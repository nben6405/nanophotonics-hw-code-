% Constants
wp = 2.4e16;
gamma = 1.1e15;
c = 3e8;

% Wavelength regime (lambda)
w_len_nm = linspace(200, 600, 50);
w_len_m = w_len_nm * 1e-9;

% Angular frequency (omega)
w = 2 * pi * c ./ w_len_m;

% Drude model // relative permittivity of aluminum
% Note the use of ./ for element-wise division
drude = 1 - (wp^2 ./ (w.^2 + 1i * gamma * w));

% Plotting
figure;
hold on;
plot(w_len_nm, real(drude), 'LineWidth', 1.5, 'DisplayName', 'Real Permittivity');
plot(w_len_nm, imag(drude), 'LineWidth', 1.5, 'DisplayName', 'Imaginary Permittivity');

xlabel('Wavelength (nm)'); % Updated label to match nm scale
ylabel('Relative Permittivity of Aluminum');
title('Aluminum Permittivity (problem 8)');
legend('show');
grid on;