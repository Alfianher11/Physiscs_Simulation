% Planetary orbit using Euler-Cromer method.
% Based on 'Computational Physics' by N. Giordano and H. Nakanishi, Section 4.1
% Written by Kevin Berwick
% Simulates a planet orbiting the Sun.

npoints = 500;        % Number of time steps
dt = 0.002;           % Time step in years

% Initialize position of the planet (in AU, Astronomical Units)
x = 1;                % Initial x position (AU)
y = 0;                % Initial y position (AU)

% Initialize velocity of the planet (in AU per year)
v_x = 0;              % Initial velocity in the x direction (AU/year)
v_y = 2 * pi;         % Initial velocity in the y direction (AU/year), 2*pi for a circular orbit

% Plot the Sun at the origin
plot(0, 0, 'oy', 'MarkerSize', 30, 'MarkerFaceColor', 'yellow'); % Sun is a yellow circle
axis([-1 1 -1 1]);     % Set axis limits from -1 to 1 in both x and y directions
xlabel('x (AU)');       % Label for x-axis (AU)
ylabel('y (AU)');       % Label for y-axis (AU)
hold on;                % Hold the plot to add the planet’s orbit

% Loop over the timesteps to simulate the planet's motion
for step = 1:npoints-1
    % Calculate the distance from the planet to the Sun (radius)
    radius = sqrt(x^2 + y^2);  % Distance formula: sqrt(x^2 + y^2)

    % Compute new velocities in the x and y directions using gravitational force
    v_x_new = v_x - (4 * pi^2 * x * dt) / (radius^3);  % Updated velocity in x direction
    v_y_new = v_y - (4 * pi^2 * y * dt) / (radius^3);  % Updated velocity in y direction

    % Euler-Cromer Step: Update position using newly calculated velocities
    x_new = x + v_x_new * dt;   % New x position
    y_new = y + v_y_new * dt;   % New y position

    % Plot the current position of the planet
    plot(x_new, y_new, '-k');   % Plot planet’s path in black
    drawnow;                    % Update plot in real-time

    % Update velocities for the next iteration
    v_x = v_x_new;  % Assign new x velocity
    v_y = v_y_new;  % Assign new y velocity

    % Update positions for the next iteration
    x = x_new;      % Assign new x position
    y = y_new;      % Assign new y position
end
