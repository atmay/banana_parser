from llvmlite import binding as llvm


def main():
    llvm.initialize()
    llvm.initialize_native_asmprinter()
    llvm.initialize_native_target()

    target = llvm.Target.from_triple("x86_64-pc-windows-msvc")
    target_machine = target.create_target_machine(codemodel='default')
    mod = llvm.parse_assembly('target triple = "x86_64-pc-windows-msvc"')

    obj = open("test.obj", "wb")
    obj.write(target_machine.emit_object(mod))
    obj.close()


if __name__ == "__main__":
    main()
