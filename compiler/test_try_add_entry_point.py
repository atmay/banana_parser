# example taken from: https://llvmlite.readthedocs.io/en/latest/user-guide/binding/examples.html
# also about LLVM:
#   Tutorial on C++
#   https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html
#   Playlist Tutorials for LLVM:
#   https://www.youtube.com/playlist?list=PLGNbPb3dQJ_5Dv45KhMlt9HMSlnfMyb2V


from __future__ import print_function
from ctypes import CFUNCTYPE, c_double
import llvmlite.binding as llvm

# All these initializations are required for code generation!
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()  # yes, even this one


def create_execution_engine():
    """
    Create an ExecutionEngine suitable for JIT code generation on
    the host CPU.  The engine is reusable for an arbitrary number of
    modules.
    """
    # Create a target machine representing the host
    # target = llvm.Target.from_default_triple()
    target = llvm.Target.from_triple("x86_64-pc-windows-msvc")
    target_machine = target.create_target_machine(codemodel='default')
    # And an execution engine with an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine, target_machine


def compile_ir(engine, llvm_ir):
    """
    Compile the LLVM IR string with the given engine.
    The compiled module object is returned.
    """
    # Create a LLVM module object from the IR
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    # Now add the module and make sure it is ready for execution
    engine.add_module(mod)
    engine.finalize_object()
    engine.run_static_constructors()
    return mod


def main():
    llvm_ir = """
       ; ModuleID = "examples/ir_entry.py"
       target triple = "x86_64-pc-windows-msvc"
       
       define i32 @main()
       {
       entry:
         ret i32 0
       }
       
       define i32 @mainCRTStartup()
       {
       entry:
         ret i32 0
       }
       """

    engine, target_machine = create_execution_engine()
    mod = compile_ir(engine, llvm_ir)

    obj = open("entry_test.obj", "wb")
    obj.write(target_machine.emit_object(mod))
    obj.close()


if __name__ == "__main__":
    main()
