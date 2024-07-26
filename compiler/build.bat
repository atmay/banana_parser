@ECHO OFF

@SET linker="C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.37.32822\bin\Hostx64\x86\link.exe"

@rem %linker% test.obj

%linker% entry_test.obj

@PAUSE
@EXIT>