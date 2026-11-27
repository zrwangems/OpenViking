x_bound = [0 100];
y_bound = [0 75];
cone_length = 30;
cone_angle = 45;
norm_vel = 6;
fast_vel = 9;
n = 200;
save('insect_sim_consts.mat','x_bound','y_bound','cone_length','cone_angle','norm_vel','fast_vel');

pred_x = ones(n,1)*10;
pred_y = ones(n,1)*70;
pred_data = [pred_x pred_y];

prey_x = ones(n,1)*70;
prey_y = ones(n,1)*10;
prey_data = [prey_x prey_y];

duration = linspace(0,24,n)';

raw_enviro_data = [pred_data, prey_data, duration];
save('raw_enviro_data.mat','raw_enviro_data');