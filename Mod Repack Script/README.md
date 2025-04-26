【YG & 他的deepseek汉化组】**nikke mod一键repack脚本**（ gjopin & 他的chatgpt ）

------

### **环境要求**

- 确保系统中已安装 **Python**。（未指定python版本）
- 使用以下命令安装所需的 Python 包：（个人推荐在IDE下执行，如pycharm或vscode）

- ```
  pip install UnityPy Pillow
  ```

  > 如果 `pip install` 无效，可尝试将 `pip` 替换为 `python`，例如：
  > `python -m pip install UnityPy Pillow`

- **创建文件夹**：
  运行脚本 `createfolders.bat` 自动生成所需目录结构。

------

### **使用 getfiles.py**

此脚本根据 JSON 文件中定义的模式，从源目录复制特定文件到目标目录。

**操作步骤**：

1. **将 JSON 配置文件与 `getfiles.py` 放在同一目录下**（若 JSON 路径不同需在脚本中指定）。
2. **运行脚本**：
   - **命令行方式**：
     打开终端或命令提示符，进入 `getfiles.py` 所在目录，执行：

1. - ```
     python getfiles.py
     ```

   - **直接运行**：
     双击 `getfiles.py` 文件。

2. **文件复制**：
   匹配的文件会从 `source_dir` 复制到与脚本同目录下的 `Original Bundles` 文件夹。

3. **解密步骤**：
   使用 **NAU 工具** 对 `Original Bundles` 文件夹进行整体解密。*（NMMv0.3.2自带NAU，位于resource/tools/NAU中）*

------

### **使用 repackscript.py**

此脚本解包修改后的资源文件，重新打包并基于原始文件模式重命名。

**操作步骤**：

1. **运行脚本**：
   - **命令行方式**：
     进入 `repackscript.py` 所在目录，执行：

1. - ```
     python repackscript.py
     ```

   - **直接运行**：
     双击 `repackscript.py` 文件。

2. **处理流程**：

   - 脚本会逐个处理修改后的文件
   - 解包资源 → 重新打包 → 根据原始文件模式重命名

3. **输出检查**：
   最终生成的打包文件（重命名后）将保存在 `Results` 文件夹中。

------

### **故障排除**

- **依赖错误**：
  确保已通过 `pip` 安装所有必需的库。
- **路径问题**（仅限 `getfiles.py`）：
  检查文件夹路径设置是否正确，且资源文件存在于指定目录。

------

按照上述步骤，您应能成功完成 Unity 资源包的导出、修改与重新打包！

如果出错的话可以向gpt求助，对脚本进行修改