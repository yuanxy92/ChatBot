% kill python server if you know pid
pid = 111111110;
system(sprintf('Taskkill /PID %d /F', pid));

% kill python server if you do not know pid (may not work)
system('Taskkill /IM python.exe /F');