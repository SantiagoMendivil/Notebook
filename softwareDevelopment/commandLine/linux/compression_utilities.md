# Table of contents
- [Table of contents](#table-of-contents)
- [Compression Utilities](#compression-utilities)
  - [Multiple Compressions](#multiple-compressions)
  - [Utilities](#utilities)

# Compression Utilities 
The compression commands reduce file sizes and differ mainly by the algorithms behind them. 

- `gzip`: retains the original file's ownership modes, access, and modification timestamps. Compressed files have the .gz extension
- `bzip2`: compressed files have the .bz2 extension 
- `xz`: compressed files have the .xz extension

The syntax to compress a file using one of these compression utilities is: 

```bash 
<compression_utility> [options] <filename> 
```

For example, the command `gzip hello.txt` will result in a compressed file named `hello.txt.gz` and delete the original file. 

Adding the `-k` option will retain the original file. 

```bash 
<compression_utility> -k <filename> 
```

## Multiple Compressions 
Multiple files can be compressed by adding all of their names as arguments or by using the wildcard symbol(*). For example: 
```bash 
bzip2 poem.txt riddle.txt
```

will result in two compressed files: `poem.txt.bz2` and `riddle.txt.bz2`. 

The command 
```bash 
xz *.txt
```

would compress all files in the current directory with the txt extension. 

## Utilities 
The `gzip` command has the ability to compress all files in a directory using the `-r` option and providing the path to a directory. 

```bash
gzip -r /path/to/directory
```

Files can be decompressed using the `-d` option. 

```bash
gzip -d hello.txt.gz
bzip2 -d poem.txt.bz2
xz -d document.txt.xz
```

