Requirement: .NET Runtime 8.0
Get it from here: https://dotnet.microsoft.com/en-us/download/dotnet/8.0

Simply drag & drop the file or folder to NikkeAssetUnpacker.exe.

NAU will automatically determine if the file is a NKAB encrypted bundle or not and decrypt if it's an encrypted one and encrypt if it's not.


NAU also supports commandline arguments that you can run through cmd or powershell

./nikkeassetunpacker.exe d -i <input folder> -o <output folder>

Output folder is optional, but if you want to decrypt everything in a folder and save it to other directory, you'll have to specify it.

For example: ./nikkeassetunpacker.exe d -i "D:\NIKKE\NIKKE\Game\Addressables\com_proximabeta\NIKKE\eb"

If you want to batch encrypt, use e instead of d.

For example: ./nikkeassetunpacker.exe e -i "D:\NIKKE\NIKKE\Game\Addressables\com_proximabeta\NIKKE\eb"

Please note that you need to omit "./" if you're using cmd, so just nikkeassetunpacker.exe d -i <input folder>