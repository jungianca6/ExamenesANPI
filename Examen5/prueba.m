clc;clear;close all
f = @(x) sin((x*pi)/2);

syms x

fs=sym(f);
fds=diff(fs);

fdn=matlabFunction(fds);

p=expand(fds)
