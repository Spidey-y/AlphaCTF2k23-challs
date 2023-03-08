# revenege

## Write-up

If you have access to rooted android device/emulator with an ARM64 Architecture:

 - Install `reflutter`
 - Run the tool on the app
 - Sign the new apk file
 - Run it in the device and dump the file `/data/data/com.example.revenge/dump.dart`
 - Knowing last year's challenge source code, get the offset for the function `_SafeState` for the class `_SafeState`.
 - Using a decompiler, decompile the function by adding the previously found offset with `_kDartIsolateSnapshotInstructions` offset
 - Get the xored flag
 - Get the offset of the function `initState` for the class `_SafeState`.
 - Get the xor value
 - Xor the list with the found value

For x86_64 rooted Android devices:

 - You must compile `libflutter.so` for x86_64 Architecture, the source code of `reflutter` and the github build file shows how its done.
 - patch `reflutter` code to add the compiled `libflutter.so`.
 - Follow the same steps from ARM64 secion starting from singing the app.