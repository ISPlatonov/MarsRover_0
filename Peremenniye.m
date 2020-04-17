x=5;
y=5;
a0=10;
a=a0;
b0=10;
h=1;
b=(b0^2+(h/2)^2)^(1/2);

xr=int32(11);
yr=int32(11);
x0=int32(4);
y0=int32(5);
xk=int32(10);
yk=int32(1);
sprx=int32([2 1 3 2 9 9 6 9 10 2 7 7 7 8 9 10 0 0 0 1 5]);
spry=int32([0 1 1 2 0 1 3 3 3 6 7 8 9 9 9 10 8 9 10 10 8]);

navput=py.Navigatsiya.navig(xr,yr,x0,y0,xk,yk,sprx,spry);
elem11=int32(str2double(char(py.Navigatsiya.elem(navput,int32(4),int32(1)))));
put=[];
for i=1:int32(str2double(char(py.Navigatsiya.len1(navput))))
    put(i,1)=int32(str2double(char(py.Navigatsiya.elem(navput,int32(i-1),int32(0)))));
    put(i,2)=int32(str2double(char(py.Navigatsiya.elem(navput,int32(i-1),int32(1)))));
end