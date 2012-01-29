function R = loadHuboCanWebots(file,joints,tl)
%Loads a HUBO data file and plots requested limbs
%'file' is the filename, including the path
%'joints' is a row vector of the requested joints
%'times' is a 2-integer row vector that has the start and end times for the
%plot, in milliseconds.
% 'theUDP' is a flag indicating whether UDP data is sent
% 'timeLength' is the amount of time, in units of milliseconds, that we
% send data
%'singleplot' determines if each joint is plotted separately. A value of 1
%means that all joints are on the same plot, otherwise they are on separate plots.


theData = csvread(file);

%size(theData)
%theData(1,1)
%theData(1,2)
%theData(1,3)

%Map joint angles to data file.
if length(joints) == 3
    if joints == 'all'
        joints = ['LSP','LSR','LSY','LEB','LWY','LW1','LW2','RSP','RSR','RSY','REB','RWY','RW1','RW2', 'RHP','RHR','RHY','RKN','RAP','RAR', 'LHP','LHR','LKN','LAR','LAP','WST'];
    end
end


w = max(size(theData))
jt = zeros(51,w);       % time
jd = zeros(51,w);       % deg

size(theData)

%% get motor deg data
ii = ones(51,1);
for i = 1:w
    jj = theData(i,2)+1;
    jt(jj, ii(jj)) = theData(i,1);      % time
    jd(jj, ii(jj)) = theData(i,3);      % deg
    ii(jj,1) = ii(jj,1)+1;
end
    


lengthvec = length(joints)/3;

v = zeros([1 lengthvec]);

%% Desired Joints
for m=1:lengthvec
    joint = joints((m-1)*3+1:(m)*3);
    JointVec{m}(1:3) = joint;
    temp = 1;
 
    switch joint
        case 'RHY'
            v(m) = 39+temp;
        case 'RHR'
            v(m) = 40+temp;
        case 'RHP'
            v(m) = 41+temp;
        case 'RKN'
            v(m) = 42+temp;
        case 'RAP'
            v(m) = 43+temp;
        case 'RAR'
            v(m) = 44+temp;
        case 'LHY'
            v(m) = 45+temp;
        case 'LHR'
            v(m) = 46+temp;
        case 'LHP'
            v(m) = 47+temp;
        case 'LKN'
            v(m) = 48+temp;
        case 'LAP'
            v(m) = 49+temp;
        case 'LAR'
            v(m) = 50+temp;
        case 'RSP'
            v(m) = 20+temp;
        case 'RSR'
            v(m) = 21+temp;
        case 'RSY'
            v(m) = 22+temp;
        case 'REB'
            v(m) = 23+temp;
        case 'LSP'
            v(m) = 24+temp;
        case 'LSR'
            v(m) = 25+temp;
        case 'LSY'
            v(m) = 26+temp;
        case 'LEB'
            v(m) = 27+temp;
        case 'RWY'
            v(m) = 0+temp;
        case 'RW1'
            v(m) = 1+temp;
        case 'RW2'
            v(m) = 2+temp;
        case 'LWY'
            v(m) = 3+temp;
        case 'LW1'
            v(m) = 4+temp;
        case 'LW2'
            v(m) = 5+temp;
        case 'NKY'
            v(m) = 6+temp;
        case 'NK1'
            v(m) = 7+temp;
        case 'NK2'
            v(m) = 8+temp;
        case 'WST'
            v(m) = 28+temp;
        otherwise
            stringerr = ['You have made an error with your joint vector number:  ', int2str(m)];
            disp(stringerr);
            return
    end
end


%% Plotting

figure
hold on
for i = 1:length(v)
   %plot(jt(v(i),:),jd(v(i),:)); 
   %plot(jt(v(i),:),jd(v(i),:)); 
   t = jt(v(i),(1:ii(v(i))-1));
   d = 180/pi*jd(v(i),(1:ii(v(i))-1));
   plot(t,d);
   %size(jt(v(i),:))
end

figure
hold on
for i = 1:length(v) 
   t = jt(v(i),(1:ii(v(i))-1));
   tt = t(1:(length(t)-1)) - t(2:length(t));
   L = (length(t)-1)
   length(t);
   length(tt);
   plot(t(1:L),tt(1:L),'.');
end
        
size(v)
size(jt)


