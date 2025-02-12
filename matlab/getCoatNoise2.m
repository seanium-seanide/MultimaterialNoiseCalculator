% dOpt   = optical thickness / lambda of each layer
%        = geometrical thickness * refractive index / lambda


function [SbrZ, StoZ, SteZ, StrZ, brLayer] = getCoatNoise2(f, lambda, wBeam, Temp, ...
  materialParams, materialSub, materialLayer, dOpt, dcdp)

  % Boltzmann const and temperature
  kBT = 1.3807e-23 * Temp;
  
  % angular frequency
  w = 2 * pi * f;
    
  % substrate properties
  alphaSub = materialParams(materialSub).alpha;
  cSub = materialParams(materialSub).C;
  kappaSub = materialParams(materialSub).kappa;
  ySub = materialParams(materialSub).Y;
  pratSub = materialParams(materialSub).prat;
  
  % make vectors of material properties
  nN = zeros(size(dOpt));
  aN = zeros(size(dOpt));
  alphaN = zeros(size(dOpt));
  betaN = zeros(size(dOpt));
  kappaN = zeros(size(dOpt));
  cN = zeros(size(dOpt));
  yN = zeros(size(dOpt));
  pratN = zeros(size(dOpt));
  phiN = zeros(size(dOpt));
  
  for n = 1:numel(materialLayer)
    nN(n) = materialParams(materialLayer(n)).n;
    aN(n) = materialParams(materialLayer(n)).a;
    alphaN(n) = materialParams(materialLayer(n)).alpha;
    betaN(n) = materialParams(materialLayer(n)).beta;
    kappaN(n) = materialParams(materialLayer(n)).kappa;
    cN(n) = materialParams(materialLayer(n)).C;
    yN(n) = materialParams(materialLayer(n)).Y;
    pratN(n) = materialParams(materialLayer(n)).prat;
    phiN(n) = materialParams(materialLayer(n)).phiM;
  end

  % geometrica thickness of each layer and total
  dGeo = lambda * dOpt ./ nN;
  dCoat = sum(dGeo);
  
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  % Brownian
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  % layer contrubutions
  brLayer = ...
    ( (1 + nN .* dcdp / 2).^2 .* (ySub ./ yN) + ...
     (1 - pratSub - 2 * pratSub.^2).^2 .* yN ./ ...
     ((1 + pratN).^2 .* (1 - 2 * pratN) .* ySub) )./ (1 - pratN) .* ((1 - pratN - 2 * pratN.^2))./((1 - pratSub - 2 * pratSub.^2));

  % sum them up for total
  SbrZ = (4 * kBT ./ (pi * wBeam^2 * w)) * ...
    sum(dGeo .* brLayer .* phiN * (1 - pratSub - 2 * pratSub.^2) / ySub);
  
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  % Thermo-optic
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  % substrate alpha
  alphaBarSub = 2 * (1 + pratSub) * alphaSub;

  % layer contrubutions
  alphaBar = (dGeo / dCoat) .* ((1 + pratSub) ./ (1 - pratN)) .* ...
    ((1 + pratN) / (1 + pratSub) + (1 - 2 * pratSub) .* yN / ySub) .* alphaN;
  
  betaBar = (-dcdp) .* dOpt .* ...
    (betaN ./ nN + alphaN .* (1 + pratN) ./ (1 - pratN));

  % thermo-elastic
  SteZ = (4 * kBT * Temp ./ (pi * wBeam^2 * sqrt(2 * kappaSub * cSub * w))) * ...
    ( sum(alphaBar * dCoat) - alphaBarSub * sum(dGeo .* cN) / cSub ).^2;
    
  % thermo-refractive
  StrZ = (4 * kBT * Temp ./ (pi * wBeam^2 * sqrt(2 * kappaSub * cSub * w))) * ...
    sum(betaBar * lambda).^2;
    
  % total thermo-optic
  StoZ = (4 * kBT * Temp ./ (pi * wBeam^2 * sqrt(2 * kappaSub * cSub * w))) * ...
    ( sum(alphaBar * dCoat) - sum(betaBar * lambda) - ...
      alphaBarSub * sum(dGeo .* cN) / cSub ).^2;
  
end
