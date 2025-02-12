% interferometer parameters
wBeam = 0.062;          % 6cm beam
lambda = 1064e-9;      % laser wavelength
Temp = 290;            % temperature

% frequencies for plotting
f = logspace(0, 2, 100)';

% make material index vector
%  the vector has one index for each coating layer
%  materialLayer(1) is the cap layer,
%  materialLayer(end) is the layer on the substrate
num21 = 19;        
num31 = 0;

numDblt = num21 + num31;
materialLayer = [repmat([1; 2], num21, 1);repmat([1; 3], num31, 1)];

% optical thickness of teach couting layer
dOpt = [ones(size(materialLayer))] * 0.25;  % all quarter-wave layers  
%% 
dOpt(1) = 0.5;
%dOpt(38) = 0;

% material index of substrate material
materialSub = 3;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% material parameters (all SI units)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

materialParams(1).name = 'SiO2';
materialParams(1).a = 2;
materialParams(1).alpha = 1e-6;
materialParams(1).beta = 1e-6;
materialParams(1).kappa = 1;
materialParams(1).C = 1e6;

materialParams(1).n = 1.45;
materialParams(1).Y = 72e9;
materialParams(1).prat = 0.17;
materialParams(1).phiM = 0.5e-4;

materialParams(2).name = 'ti-silica';
materialParams(2).a = 0;
materialParams(2).alpha = 1e-6;
materialParams(2).beta = 1e-6;
materialParams(2).kappa = 1;
materialParams(2).C = 1e6;

%materialParams(2).n = 1.97;
%materialParams(2).Y = 97e9;
%materialParams(2).prat = 0.27;
%materialParams(2).phiM = 3.1e-4;

%tantala
materialParams(2).n = 2.07;
materialParams(2).Y = 140e9;
materialParams(2).prat = 0.28;
materialParams(2).phiM = 3.3e-4;

materialParams(3).name = 'SiO2 substrate';
materialParams(3).a = 0;
materialParams(3).alpha = 1e-6;
materialParams(3).beta = 1e-6;
materialParams(3).kappa = 1;
materialParams(3).C = 1e6;

materialParams(3).n = 1.45;
materialParams(3).Y = 73.2e9;
materialParams(3).prat = 0.17;
materialParams(3).phiM = 1e-9;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% build layer vectors for later use
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% substrate properties
nSub = materialParams(materialSub).n;
ySub = materialParams(materialSub).Y;
pratSub = materialParams(materialSub).prat;

% make vectors of material properties
nLayer = zeros(size(dOpt));
aLayer = zeros(size(dOpt));

for n = 1:numel(materialLayer)
  nLayer(n) = materialParams(materialLayer(n)).n;
  aLayer(n) = materialParams(materialLayer(n)).a;
end

%nLayer

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% compute coating properties
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% compute reflectivies
[rCoat, dcdp, rbar, r] = getCoatRefl2(1, nSub, nLayer, dOpt);
%dcdp = 0;


% compute absorption
[absCoat, absLayer, powerLayer, rho] = ...
  getCoatAbsorption(lambda, dOpt, aLayer, nLayer, rbar, r);

% compute brownian and thermo-optic noises
[SbrZ, StoZ, SteZ, StrZ, brLayer] = getCoatNoise2(f, lambda, wBeam, Temp, ...
  materialParams, materialSub, materialLayer, dOpt, dcdp);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% make some plots
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% absorption values

figure(1)
clf
semilogy([rho, powerLayer, rho .* powerLayer], 'o', ...
                       'MarkerFaceColor',[0.8, 0.8, 0.8],...
                       'MarkerSize',10)
grid on
legend({'$\rho_j$', '$P_j / P_0$', '$\bar{\rho}_j$'}, 'interpreter', 'latex')
xlabel('layer number')
title('Absorption Values')
orient rotated
%print -dpdf ../plot/rho.pdf

% noise weights for each layer
figure(2)
clf
plot([-dcdp, brLayer], 'o', ...
  'MarkerFaceColor',[0.8, 0.8, 0.8], 'MarkerSize',10)
grid on
legend({'$-\partial\phi_c / \partial\phi_j$', '$b_j$'}, 'interpreter', 'latex')
xlabel('layer number')
title('Noise Weights for Each Layer')
orient rotated
%print -dpdf ../plot/dcdp.pdf

% noise plots
figure(3)
clf
loglog(f, sqrt(SbrZ), 'r')
hold on
loglog(f, sqrt(StoZ), 'b')
loglog(f, sqrt(SteZ), '-.', 'Color', [0.5, 0.2, 1])
loglog(f, sqrt(StrZ), '-.', 'Color', [0.2, 0.5, 1])
hold off
grid on
legend('Brownian Noise', 'Thermo-optic Noise', ...
  'TE Component', 'TR Component')
xlabel('frequency [Hz]')
ylabel('thermal noise [m/\surd Hz]')
title('Noise Plots')
%ylabel('thermal noise [$m/\sqrt{\rm Hz}$]', 'interpreter', 'latex')
orient rotated
%print -dpdf ../plot/ctn.pdf

% Why lol
%sqrt(SbrZ(100))
