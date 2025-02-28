% [absCoat, absLayer, powerLayer, rho] = ...
%        getCoatAbsorption(lambda, dOpt, aLayer, nLayer, rbar, r)
%   returns coating absorption as a function of depth
%
% lambda = wavelength
% dOpt   = optical thickness / lambda of each layer
%        = geometrical thickness * refractive index / lambda
% aLayer = absorption per unit length in each layer
% nLayer = refractive index of each layer, ordered input to output (N x 1)
% rbar = amplitude reflectivity of coating from this layer down
% r = amplitude reflectivity of this interface (r(1) is nIn to nLayer(1))
%
% rho = power ratio in each layer
% absLayer = absorption contribution form each layer
% absCoat = coating total absorption = sum(absLayer)
%
% see getCoatRefl2

function  [absCoat, absLayer, powerLayer, rho] = ...
  getCoatAbsorption(lambda, dOpt, aLayer, nLayer, rbar, r)
  
  % power in each layer
  powerLayer = cumprod(abs((1 - r(1:end-1).^2) ./ ...
    (1 + r(1:end-1) .* rbar).^2));

  % one-way phases in each layer
  phi = 2 * pi * dOpt;

  % average E-field squared in each layer
  rho = (1 + abs(rbar).^2) + 2 * (sin(phi) ./ phi) .* ...
    real(rbar .* exp(1i * phi));
  
  % ???? Dimensionally, this is not correct
  % geometrical thickness of each layer
  dGeo = lambda * dOpt ./ nLayer;
  
  % compute power weighting for each layer
  absLayer = aLayer .* rho .* powerLayer .* dGeo;
  
  % total coating absorption
  absCoat = sum(absLayer);
end
