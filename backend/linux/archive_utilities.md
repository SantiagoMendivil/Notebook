# Table of contents 
- [Table of contents](#table-of-contents)
- [Archive Utilities](#archive-utilities)
  - [zip](#zip)
  - [tar](#tar)
    - [Options to compress with tar](#options-to-compress-with-tar)
      - [gzip](#gzip)
      - [bzip2](#bzip2)
      - [xz](#xz)

# Archive Utilities
Archiving allows us to consolidate multiple files or directories into a single archived file. 

- `zip`
- `tar`

## zip
Zip files are very popular across multiple operating systems. We can create a .zip archive like so: 

```bash 
zip <archive_name>.zip <file1> <file2> ...
```

**Note**: Sometimes zip must be installed first using:

```bash 
sudo apt install zip unzip
```

Directories can be easily archived with the -r option and extracted with unzip command and providing paths to one or more .zip files. 

## tar
Stands for tape archive or tarball, is a very important archiving utility for Linux systems. While a zip archive is more popular across platforms, it is recommended to use tar when distributing archives among Linux-based systems

This because tar archives store Unix file attributes. 

```bash 
tar -cf <archive_name>.tar <files or directories>
```

This command creates an uncompressed .tar archive. This can be referred to as tarball. For example: 

```bash 
tar -cf example.tar index.html script.js style.css
```
will create a .tar archive file with three files. 

```bash 
tar -xf <archive_name>.tar
```
This last command will extract the files from the tar file. 

### Options to compress with tar 
We can combine with the compression utilities. tar with the -c and -f options relate to archiving functionalities, but we can also call tar with other options to compress: 

#### gzip
- -z: Compress the resulting archive using gzip. Resulting file extension: .tar.gz 

Example:
```bash 
tar -czf archive.tar.gz file1 file2
```
Use case: Suitable for general-purpose compression, widely supported and faster compression/decompression.

#### bzip2
- -j: Compress the resulting archive using bzip2. Resulting file extension: .tar.bz2

Example:
```bash 
tar -cjf archive.tar.bz2 file1 file2
```
Use case: Provides better compression ratio than gzip, but slower. Ideal for compressing large files where space saving is critical.

#### xz
- -J: Compress the resulting archive using xz. Resulting file extension: .tar.xz 

Example:
```bash 
tar -cJf archive.tar.xz file1 file2
```
Use case: Offers the highest compression ratio among the three, but the slowest. Best for scenarios where maximum compression is needed and time is not a constraint.

In order to compress an archive/tarball of some video files where we want the resulting compressed archive to be called videos.tar.bz2 we use the following command: 

```bash 
tar -cjf videos.tar.bz2 video1.mp4 video2.mkv
```