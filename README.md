# Conan_samples
This repository contains various Conan/python samples.
```
git.exe clone --progress --recursive -v "git@github.com:dudasl/Conan_samples.git" "D:\Conan_samples"
```

## SetBuildNumber
This project demonstrates how we can change a simple file that contains a
version number in format **major.minor.patch.build**. The goal is to modify the
line in the file that starts with "*version:*" with the passed build number.

1. Open the solution [SetBuildNumber.sln](SetBuildNumber/SetBuildNumber.sln) in Visual Studio
2. Open properties of the project **SetBuildNumber** and in **Debug** tab set
two **Script Arguments**:
    - First argument represents the path to the file
    - Second argument represents the build number
3. Run the program using **Debug** -> **Start Debugging**

## HelloWorld
Classic simple "Hello world" console application just for demonstration purpose.
Used as a submodule.
