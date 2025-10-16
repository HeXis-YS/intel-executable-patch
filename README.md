# intel-executable-patch

A python script that can patch executables and libraries compiled with Intel compiler (or Intel MKL), for better performance on **ANY non-Intel** X86 processors.

Before running the script, **make backup copies of your binaries**! This is because the patching is irreversible and it might break softwares.
**Use it at your own risk.**

Run the script with Python:

```bash
python patch.py exe
```

This will modify the jump instructions or results of the Intel CPUID dispatcher.

### Experimental Usage

You can obtain a patched Intel toolchain by running the following command.

```bash
cd /opt/intel/oneapi/compiler/latest
sudo find bin lib -type f -exec python patch.py {} \;
```

The toolchain itself and any program compiled using it incorporate the patch from this script.

**Please ensure you comply with Intel's EULA. I am not responsible for any legal disputes that may arise.**
