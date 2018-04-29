clc
clear

data_all=[];
t = tcpip('127.0.0.1', 54377, 'Timeout', 60,'InputBufferSize',10240);

ind = 0;
while(1)
    fopen(t);
    buf = input('please input an string:\n','s');
    fwrite(t, buf);
    while(1) 
        nBytes = get(t,'BytesAvailable');
        if nBytes>0
            break;
        end
    end
    receive = fread(t,nBytes);
    fprintf('%s\n', receive);
    fclose(t);
    pause(0.0001);
end
delete(t);