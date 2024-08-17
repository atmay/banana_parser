@ECHO OFF

@SET linker="C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x86\link.exe"

@SET linker="F:\PROGRAMMS\clang+llvm-18.1.8-x86_64-pc-windows-msvc\bin\llvm-link.exe"


%linker% entry_test.obj

@PAUSE
@EXIT>