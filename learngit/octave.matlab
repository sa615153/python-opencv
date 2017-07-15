size of variable/matrix 不用事先定义
a=[]
a(1)=2
a(2)=3
a(2,1)=11
a(2,2)=5


p3 = linspace(1,3,5)  返回线性行向量

行向量和列向量的索引方式相同，都是v(i)

surf
If only a single Z matrix is given, then it is plotted over the meshgrid 'X = 1:columns (Z), Y = 1:rows (Z)'.






%%%%%%%%%%%plot%%%%%%%%%%
plot(x,y,'rx','MarkerSize',10) % plot(x,y) plot(x,y,'r') default draw line % plot(x, y, 'o-r') circle with lines
plot(X_0(:,1),X_0(:,2),'ko','MarkerFaceColor','y');

%%%%%%%auto lengend%%%%%%
for i = 1:length(learning_rate)
  fprintf('inside for loop: %d alpha:%d \n',i,learning_rate(i));

% [theta, J_history] = gradientDescentMulti(X, y, theta, learning_rate(i), num_iters);
  [theta, J_history] = gradientDescentMulti(X, y, [0;0;0], learning_rate(i), num_iters);
  plot(J_history);
  hold on;
  legendInfo{i} = ['alpha = ' num2str(learning_rate(i))];
%  pause;
 end
 
legend(legendInfo);










fprintf(' x = [%.0f %.0f], y = %.0f \n', [X(1:10,:) y(1:10,:)]');这种格式化字符串也可以，结果
			x = [2104 3], y = 399900
			x = [1600 3], y = 329900
			x = [2400 3], y = 369000
			x = [1416 2], y = 232000
			x = [3000 4], y = 539900
			x = [1985 4], y = 299900
			x = [1534 3], y = 314900
			x = [1427 3], y = 198999
			x = [1380 3], y = 212000
			x = [1494 3], y = 242500					


size(X,1) 行数
size(X,1) 列数

mean()
 If X is a matrix, compute the mean for each column and return them in a row vector.
 If the optional argument DIM is given, operate along this dimension.


std()
If X is a matrix, compute the standard deviation for each column and return them in a row vector.


mod()
y  = 1 + mod(1:m, num_labels)'; %mod 1参数mod 2参数

遇到一情况：
sigma是一行二列[794.70235     0.76098]
原想法：先变成倒数行向量，再左乘ones(n,1)来复制多行：
for_div_1 = ones(1,n)./sigma;
for_div_2 = ones(n,1) * for_div_1;
%for_div_3 = for_div_2 .* eye(n);
现发现可用一条命令完成--不同维数犯规做点除
ones(n,1)./sigma

  
sprintf('inside for loop: %f',i); 不输出
fprintf('inside for loop: %f',i); 正确打印





surf()
% Because of the way meshgrids work in the surf command, we need to
% transpose J_vals before calling surf, or else the axes will be flipped
J_vals = J_vals';
% Surface plot
figure;
surf(theta0_vals, theta1_vals, J_vals)
xlabel('\theta_0'); ylabel('\theta_1');

% Contour plot
figure;
% Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
xlabel('\theta_0'); ylabel('\theta_1');
hold on;
plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);


'legistic regression reg decision boundary'
    % Here is the grid range
    u = linspace(-1, 1.5, 50);
    v = linspace(-1, 1.5, 50);

    z = zeros(length(u), length(v));
    % Evaluate z = theta*x over the grid
    for i = 1:length(u)
        for j = 1:length(v)
            z(i,j) = mapFeature(u(i), v(j))*theta;
        end
    end
    z = z'; % important to transpose z before calling contour

    % Plot z = 0
    % Notice you need to specify the range [0, 0]
    contour(u, v, z, [0, 0], 'LineWidth', 2)








%%%%%%%%%%%bug：
原因是用了没有featureNormalize的数据去跑gradient descent
warning: opengl_renderer: data values greater than float capacity.  (1) Scale data, or (2) Use gnuplot
warning: opengl_renderer: data values greater than float capacity.  (1) Scale data, or (2) Use gnuplot

convert to string
a = [1,2,3,4,5]
str = mat2str(a)
str = '[1,2,3,4,5]'


修改过的代码，保存后，运行的还是原来的代码
办法：重启octave

subscripts must be either integers 1 to (2^31)-1 or logicals
g = 1./(exp(-z)+1) * (1 - 1./(exp(-z)+1));  代码中的乘法要用*，不能省略




%%%%%%%%%%%%%%%%%%%%%%%%%%%cell array%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
A square bracket creates a vector or matrix, whereas curly brackets creates a cell array
和matrix基本一样，索引或者逻辑，只是里边的cell可以存储任何类型的数据，包括一个cell里存储matrix
x = [1 2 3]; #% matrix with values 1, 2, 3
y = {1, 'a', x}; #% cell array storing a number, a character, and 1x3 matrix


create:
C = {}
emptyCell = cell(3,4,2)
(:,:,1) = 
    []    []    []    []
    []    []    []    []
    []    []    []    []

(:,:,2) = 
    []    []    []    []
    []    []    []    []
    []    []    []    []




C = {'one', 'two', 'three'; 
     1, 2, 3}
上键下值，其实无所谓键值，都是cell而已，我受python的dict影响了
%     C =
% {
%   [1,1] = one
%   [2,1] =  1
%   [1,2] = two
%   [2,2] =  2
%   [1,3] = three
%   [2,3] =  3
% }

upperLeft = C(1:2,1:2)
% upperLeft 
%     'one'    'two'
%     [  1]    [  2]

C(1,1:3) = {'first','second','third'}

If cells in your array contain numeric data, 
you can convert the cells to a numeric array using the cell2mat function.%
numericCells = C(2,1:3)
numericVector = cell2mat(numericCells)

curly braces{}
last = C{2,3}
C{2,3} = 300
    % 2×3 cell array
    % 'first'    'second'    'third'
    % [    1]    [     2]    [  300]

[r1c1, r2c1, r1c2, r2c2] = C{1:2,1:2}%MATLAB® returns the contents of the cells as a comma-separated list. Because each cell can contain a different type of data, you cannot assign this list to a single variable. However, you can assign the list to the same number of variables as cells. 
% r1c1 = 
% 'first'
% r2c1 = 1
% r1c2 = 
% 'second'
% r2c2 = 2

If each cell contains the same type of data, you can create a single variable by applying the array concatenation operator, [], 
 to the comma-separated list.
Concatenate the contents of the second row into a numeric array.
nums = [C{2,:}]

>> t(1,:) = {'str1',[1,2,4]};
>> t(2,:) = {'str2',[4,5,6]};
>> t(3,:) = {'str3',[7,8,9]};
左键右值，其实无所谓键值，都是cell而已，我受python的dict影响了
>> t
% t =
% {
%   [1,1] = str1
%   [2,1] = str2
%   [3,1] = str3
%   [1,2] =
%      1   2   4
%   [2,2] =
%      4   5   6
%   [3,2] =
%      7   8   9
% }
For example, store temperature data for three cities over time in a cell array.这是个cell array，temperature的每一行都是个cell
temperature(1,:) = {'2009-12-31', [45, 49, 0]};
temperature(2,:) = {'2010-04-03', [54, 68, 21]};
temperature(3,:) = {'2010-06-20', [72, 85, 53]};
temperature(4,:) = {'2010-09-15', [63, 81, 56]};
temperature(5,:) = {'2010-12-09', [38, 54, 18]};
左键右值，其实无所谓键值，都是cell而已，我受python的dict影响了
% temperature
% temperature = 5×2 cell array
%     '2009-12-31'    [1×3 double]
%     '2010-04-03'    [1×3 double]
%     '2010-06-20'    [1×3 double]
%     '2010-09-15'    [1×3 double]
%     '2010-12-09'    [1×3 double]

Plot the temperatures for each city by date.

allTemps = cell2mat(temperature(:,2));
dates = datetime(temperature(:,1));

plot(dates,allTemps)
title('Temperature Trends for Different Locations')
xlabel('Date')
ylabel('Degrees (Fahrenheit)')







struct arrays
>> p(1).name = 'A';
>> p(1).billing = 127.00;
>> p(1).test = [1,2,3;4,5,6;7,8,9];
>> p(2).name = 'B';
>> p(2).billing = 254.00;
>> p(2).test = [9,8,7;6,5,4;3,2,1];
>> p
% p =
%   1x2 struct array containing the fields:
%     name
%     billing
%     test

%%%%%%%%%%%%%%%%%%%%%%%%%%%INDEX%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%index
>> a = magic(5)
a =

   17   24    1    8   15
   23    5    7   14   16
    4    6   13   20   22
   10   12   19   21    3
   11   18   25    2    9

>> a([1,2,3,4,5])
ans =

   17   23    4   10   11

>> a([1;2;3;4;5])
ans =

   17
   23
    4
   10
   11

>>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%





%%%%%%%%%%%judgetype%%%%%%%%%%%%%%%%

if isscalar(z) == 1,
  disp('this is a scalar');
  g = 1/(1+exp(-z));
  
elseif isvector(z) == 1,
  disp('vector');
  g = 1./(exp(-z)+1);
  
elseif ismatrix(z),
  disp('matrix');
  g = 1./(exp(-z)+1);
end;







%%%%%%%%%%%shift of matlab%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Shifting
6.1 Vectors
To shift and rotate the elements of a vector, use
X([ end 1:end-1 ]); % shift right/down 1 element
X([ end-k+1:end 1:end-k ]); % shift right/down k elements
X([ 2:end 1 ]); % shift left/up 1 element
X([ k+1:end 1:k ]); % shift left/up k elements
Note that these only work if k is non-negative. If k is an arbitrary integer one may use something
like
X( mod((1:end)-k-1, end)+1 ); % shift right/down k elements
X( mod((1:end)+k-1, end)+1 ); % shift left/up k element
where a negative k will shift in the opposite direction of a positive k.

6.2 Matrices and arrays     cell is ok
To shift and rotate the elements of an array X along dimension dim, first initialize a subscript cell
array with
idx = repmat({’:’}, ndims(X), 1); % initialize subscripts
n = size(X, dim); % length along dimension dim
then manipulate the subscript cell array as appropriate by using one of
idx{dim} = [ n 1:n-1 ]; % shift right/down/forwards 1 element
idx{dim} = [ n-k+1:n 1:n-k ]; % shift right/down/forwards k elements
idx{dim} = [ 2:n 1 ]; % shift left/up/backwards 1 element
idx{dim} = [ k+1:n 1:k ]; % shift left/up/backwards k elements
finally create the new array
Y = X(idx{:});





%%%%%%%%%%%%%%%%reverse  flip%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

insert element to the front of a cell 

legendInfo = fliplr(legendInfo)
legendInfo{end + 1} = ['neg']
legendInfo{end + 1} = ['pos']
legendInfo = fliplr(legendInfo)
legend(legendInfo)






%%%%%%%%%%fminunc%%%%%make a @(t)(costFunction(t, X, y))%%%%%%%%%%%
options= optimset('GradObj', 'on', 'MaxIter', '100'); % define the options data structure
initialTheta= zeros(2,1); # set the initial dimensions for theta % initialize the theta values
[optTheta, funtionVal, exitFlag]= fminunc(@costFunction, initialTheta, options); % run the algorithm

GradObj option to on, which tells fminunc that our function returns both the cost and the gradient.

%Input for the cost function is THETA, which is a vector of the θ parameters
%Two return values from costFunction are
jval
	How we compute the cost function θ (the underived cost function) 
	In this case = (θ1 - 5)2 + (θ2 - 5)2
gradient
	2 by 1 vector
	2 elements are the two partial derivative terms
	i.e. this is an n-dimensional vector
	Each indexed value gives the partial derivatives for the partial derivative of J(θ) with respect to θi
	Where i is the index position in the gradient vector 


% Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);
% Run fminunc to obtain the optimal theta
% This function will return theta and the cost
[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial theta, options);
% use a \short-hand"for specifying functions with the @(t) ( costFunction(t, X, y) ) . This
'creates a function, with argument t', which calls your costFunction. This
% allows us to wrap the costFunction for use with fminunc.




%%%%%%%%%%%%%reshape%%%%%%%%%%%%%%%%

reshape(X(curr_ex, :), example_height, example_width)


 reshape(1:15,5,3)
ans =

    1    6   11
    2    7   12
    3    8   13
    4    9   14
    5   10   15




%%%%%%%%%%%%%function%%%%%%%%%%%%%%%%
单行定义函数：(逗号，分号*，endfunction)
function y = ferr (s, x), y = "MyString"; endfunction

多行定义函数：
function p = predict(Theta1, Theta2, X)
p = ...
end



%%%%%%%%%%%%% apply function to each element %%%%%%%%%%%%%%%%
%https://www.gnu.org/software/octave/doc/interpreter/Function-Application.html
function y = myfunc(x),y = 2*x;endfunction
a = [1 2 3 4 5]
arrayfun(@myfunc,a)
'----to two array----'
arrayfun (@atan2, [1, 0], [0, 1])
%[ 1.57080   0.00000 ]
'----change return value from matrix to cell----'
arrayfun (@(x,y) x:y, "abc", "def", "UniformOutput", false)

% arrayfun (@(x,y) x:y, "abc", "def", "UniformOutput", false)
% ⇒
%    {
%      [1,1] = abcd
%      [1,2] = bcde
%      [1,3] = cdef
%    }

% [A, B, C] = arrayfun (@find, [10; 0], "UniformOutput", false)
% ⇒
% A =
% {
%    [1,1] =  1
%    [2,1] = [](0x0)
% }
% B =
% {
%    [1,1] =  1
%    [2,1] = [](0x0)
% }
% C =
% {
%    [1,1] =  10
%    [2,1] = [](0x0)
% }

'--------my example : change y from 1-10 to vectors--------------'

function v = scalar2vector(x),
  if x == 1,
    v = [1;0;0;0;0;0;0;0;0;0];
  elseif x == 2,
    v = [0;1;0;0;0;0;0;0;0;0];
  elseif x == 3,
    v = [0;0;1;0;0;0;0;0;0;0];
  elseif x == 4,
    v = [0;0;0;1;0;0;0;0;0;0];
  elseif x == 5,
    v = [0;0;0;0;1;0;0;0;0;0];
  elseif x == 6,
    v = [0;0;0;0;0;1;0;0;0;0];
  elseif x == 7,
    v = [0;0;0;0;0;0;1;0;0;0];
  elseif x == 8,
    v = [0;0;0;0;0;0;0;1;0;0];
  elseif x == 9,
    v = [0;0;0;0;0;0;0;0;1;0];
  elseif x == 10,
    v = [0;0;0;0;0;0;0;0;0;1];
  end
endfunction

Y = arrayfun(@scalar2vector,y,"UniformOutput",false);
















































给row赋值->列向量vectoe
>> a = magic(5)

   17   24    1    8   15
   23    5    7   14   16
    4    6   13   20   22
   10   12   19   21    3
   11   18   25    2    9

>> a(2,:) = [1;1;1;1;1]
a =

   17   24    1    8   15
    1    1    1    1    1
    4    6   13   20   22
   10   12   19   21    3
   11   18   25    2    9



字符串数组要用cell，用matrix的后果是索引时理解为一个大字符串
用contours画不规则decision boundrary