% Parameters
E = 1.5;      
V = 1.0;      

% wave nums
k1 = 6.27*10^9; 
k2 = 3.625*10^9;

% Calculate Reflection and Transmission amplitudes
r = (k1 - k2) / (k1 + k2);
t = (2 * k1) / (k1 + k2);

% regions
x1 = linspace(-20, 0, 100); % region 1
x2 = linspace(0, 20, 100);  % region 2

% wavefuncs for region 1 and 2
psi1 = exp(1i*k1*x1) + r*exp(-1i*k1*x1);
psi2 = t*exp(1i*k2*x2);

% probability density 
P1 = abs(psi1).^2;
P2 = abs(psi2).^2;

% Plotting
figure('Color', 'w');
plot(x1, P1, 'b', 'LineWidth', 2); hold on;
plot(x2, P2, 'r', 'LineWidth', 2);
xline(0, '--k', 'Barrier Interface');
grid on;

% Labeling
title('Probability Density P(x) for E > V');
xlabel('Position (x)');
ylabel('P(x) = |\psi(x)|^2');
legend('Region I (Interference)', 'Region II (Transmission)');

% Display Key Values
fprintf('Reflectance Amplitude (r): %.4f\n', r);
fprintf('Reflectance (R = r^2): %.4f\n', r^2);
fprintf('Max P(x) in Region I: %.4f\n', (1+abs(r))^2);
fprintf('Min P(x) in Region I: %.4f\n', (1-abs(r))^2);
fprintf('Constant P(x) in Region II: %.4f\n', abs(t)^2);