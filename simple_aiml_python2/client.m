% clear
clear;
clc;
fclose all;

% run python server
python_dir = 'E:\\Project\\ChatBot\\simple_aiml_python2\\python_server';
system(sprintf('cmd.exe /k %s\\run_in_anaconda.bat %s &', python_dir, python_dir));
% if you want the window of python server to be close automatically, use /c
% to replace /k
% system(sprintf('cmd.exe /c %s\\run_in_anaconda.bat %s &', python_dir, python_dir));

fprintf('Wait for some seconds, the aiml server need some time to start!\n');
pause(7);

% create tcpip link
t = tcpip('127.0.0.1', 54377, 'Timeout', 1, 'InputBufferSize', 10240);
% get pid which can be used to kill python aiml server
fopen(t);
fwrite(t, 'getpid');
while(1) 
    nBytes = get(t,'BytesAvailable');
    if nBytes>0
        break;
    end
    pause(0.05);
end
receive = fread(t, nBytes);
pid = int64(str2double(char(receive)));
fclose(t);

% start talking
ind = 0;
while(1)
    buf = input('please input an string:\n','s');
    % type exit to exit the program
    try
        fopen(t);
        if strcmpi(buf, 'exit')
            break;
        end
        fwrite(t, buf);
    catch error
        fprintf('Connection refused');
        break;
    end
    while(1) 
        nBytes = get(t,'BytesAvailable');
        if nBytes>0
            break;
        end
        pause(0.05);
    end
    receive = fread(t,nBytes);
    str = char(receive);
    fprintf('%s\n', str);
    fclose(t);
    pause(0.0001);
end
delete(t);

% kill python server
system(sprintf('Taskkill /PID %d /F', pid));