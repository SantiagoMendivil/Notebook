# Table of contents
- [Table of contents](#table-of-contents)
- [ls](#ls)
- [bzip2](#bzip2)
  - [Compress with bzip2](#compress-with-bzip2)
  - [Decompress with bzip2](#decompress-with-bzip2)
- [gzip](#gzip)
  - [Compress all the files in a directory](#compress-all-the-files-in-a-directory)
- [xz](#xz)
  - [Compress using xz](#compress-using-xz)
- [zip](#zip)
  - [Compress to zip file](#compress-to-zip-file)
  - [Compress a directory into a zip file](#compress-a-directory-into-a-zip-file)
  - [Decompress a zip file](#decompress-a-zip-file)
- [tar](#tar)
  - [Compress to tar file](#compress-to-tar-file)
  - [Decompress from tar file](#decompress-from-tar-file)
  - [compress tar with gzip](#compress-tar-with-gzip)
  - [compress tar with bzip2](#compress-tar-with-bzip2)
  - [compress tar with xz](#compress-tar-with-xz)
  - [Decompress with that pattern](#decompress-with-that-pattern)
- [curl](#curl)
  - [Display content from url](#display-content-from-url)
  - [Download online file to a file name](#download-online-file-to-a-file-name)
- [Build a Build Script](#build-a-build-script)

# ls 
Using

```bash 
ls -R
```

will display all the files in the current directory and subdirectories. 


# bzip2 
We can commpress multiple files by specifying them in one line. For example:

## Compress with bzip2

```bash 
bzip2 hello.txt bye.txt
```

## Decompress with bzip2 

```bash 
bzip2 -d <directory_name>/*.bz2
```

This command selects all the files from the directory with the extension bz2. 


# gzip
## Compress all the files in a directory 

```bash 
gzip -r <directory_name>
```


# xz 
## Compress using xz 

```bash 
xz -k <file_name> 
```


# zip
## Compress to zip file
```bash 
zip <archive_name>.zip <file1> <file2> 
```


## Compress a directory into a zip file

```bash
zip <archive_name>.zip -r <directory_name>
```

## Decompress a zip file 
```bash
unzip <archive_name>.zip
```


# tar
## Compress to tar file
```bash 
tar -cf example.tar index.html script.js style.css
```

## Decompress from tar file 
```bash 
tar -xf <archive_name>.tar
```

## compress tar with gzip
- -z: Compress the resulting archive using gzip. Resulting file extension: .tar.gz 

Example:
```bash 
tar -czf archive.tar.gz file1 file2
```
Use case: Suitable for general-purpose compression, widely supported and faster compression/decompression.

## compress tar with bzip2
- -j: Compress the resulting archive using bzip2. Resulting file extension: .tar.bz2

Example:
```bash 
tar -cjf archive.tar.bz2 file1 file2
```
Use case: Provides better compression ratio than gzip, but slower. Ideal for compressing large files where space saving is critical.

## compress tar with xz
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

## Decompress with that pattern 
Just change the -c with -x 



# curl

## Display content from url
```bash 
curl "exampleurl.com"
```

## Download online file to a file name
```bash 
curl "exampleurl.com" --output file_name
```


# Build a Build Script 
