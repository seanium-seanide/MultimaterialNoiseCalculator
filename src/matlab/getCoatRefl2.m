% [rCoat, dcdp, rbar, r] = getCoatRefl2(nIn, nOut, nLayer, dOpt)
%   returns coating reflection and phase derivatives
%
% nIn = refractive index of input medium (e.g., vacuum = 1)
% nOut = refractive index of output medium (e.g., SiO2 = 1.45231 @ 1064nm)
% nLayer = refractive index of each layer, ordered input to output (N x 1)
% dOpt   = optical thickness / lambda of each layer
%        = geometrical thickness * refractive index / lambda
%
% rCoat = amplitude reflectivity of coating (complex) = rbar(0)
% dcdp = d reflection phase / d round-trip layer phase
% rbar = amplitude reflectivity of coating from this layer down
% r = amplitude reflectivity of this interface (r(1) is nIn to nLayer(1))
%
% see GWINC getCoatRefl and getCoatTOPhase for more information
% (see also T080101)

function  [rCoat, dcdp, rbar, r] = getCoatRefl2(nIn, nOut, nLayer, dOpt)

  % vector of all refractive indexs
  nAll = [nIn; nLayer(:); nOut];
  
  % reflectivity of each interface
  r = (nAll(1:end-1) - nAll(2:end)) ./ (nAll(1:end-1) + nAll(2:end));
  
  % combine reflectivities
  rbar = zeros(size(r));
  ephi = zeros(size(r));
  
  ephi(end) = exp(-4i * pi * dOpt(end));
  rbar(end) = ephi(end) * r(end);
  for n = numel(dOpt):-1:1
    % round-trip phase in this layer
    if n > 1
      ephi(n) = exp(-4i * pi * dOpt(n - 1));
    else
      ephi(n) = 1;
    end
    
    % accumulate reflecitivity
    rbar(n) = ephi(n) * (r(n) + rbar(n + 1)) / (1 + r(n) * rbar(n + 1));
  end
  
  % reflectivity derivatives
  dr_dphi = zeros(size(dOpt));
  for n = numel(dOpt):-1:1
    dr_dphi(n) = -1i * rbar(n + 1);
    for m = n:-1:1
      dr_dphi(n) = dr_dphi(n) * ephi(m) * ...
        (1 - r(m).^2) / (1 + r(m) * rbar(m + 1)).^2;
    end
  end

  % shift rbar index
  rCoat = rbar(1);
  rbar = rbar(2:end);
  
  % phase derivatives
  dcdp = imag(dr_dphi / rCoat);

end
