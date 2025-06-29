% Constants
h = 6.626e-34; % Planck constant
c = 2.998e8; % Speed of light
k = 1.381e-23; % Boltzmann constant

% Wavelength range (meters)
lambda = linspace(1e-10, 3e-6, 10000);

% Temperature (Kelvin)
T = 1e7;

% Blackbody radiation equation
B_lambda = (2*h*c^2)./((lambda.^5).*(exp((h*c)./(lambda*k*T))-1));

% Plot the result
figure;
plot(lambda*1e9, B_lambda);
xlabel('Wavelength (nm)');
ylabel('Flux density (W/m^2/nm)');
title(['Blackbody radiation at T = ', num2str(T), ' K']);
