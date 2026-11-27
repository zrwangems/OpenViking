function sfRobotScene(dock,width,boxes,circles)

plot(nsidedpoly(8,Center=dock,Radius=2*width),FaceColor="green");
daspect([1 1 1])
hold on

for i = 1:height(circles)
    center = circles(i,1:2);
    radius = circles(i,3);
    plot(nsidedpoly(20,Center=center,Radius=radius),FaceColor="red");
end

for i = 1:height(boxes)
    box = boxes(i,:);
    X = [box(1) box(1)+box(3) box(1)+box(3) box(1)];
    Y = [box(2) box(2) box(2)-box(4) box(2)-box(4)];
    plot(polyshape(X,Y),FaceColor="red");
end

fig = gcf;
fig.Name = "Robot Obstacle Course";
fig.NumberTitle = 'off';
figure(fig)

end