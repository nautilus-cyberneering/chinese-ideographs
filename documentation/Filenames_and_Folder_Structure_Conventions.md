# Filenames and Folder Structure Conventions

For codes explanation see [File Naming Convention](File_Naming_Convention.md)

## Format

```text
{ARTWORK_ID}-{PURPOSE_CODE}.{TRANSFORMATION_CODE}.{TYPE_CODE}.tif
```

Example:

```text
000001-32.600.2.tif
```

That is the original (no transformation) gold image from artwork with ID 000001.

Example:

```text
000001.52.600.2.tif
```

That is the original (no transformation) base image from artwork with ID 000001.

Artwork ID: manually assigned between 000000 and 999999 for drawings.

```generic

Scheme Version: v.0.1.0

.Nautilus Namecodes            (((0x000 - 0x93F)))
│   
├── BASICTYPE                   ((0x000 - 0x00F))
│   └── BasicType                (0x000 - 0x00F)
│       └── basictype             0x000 - 0x00F
│       
│   
├── PURPOSE                     ((0x030 - 0x06F))
│   └── Purposes                 (0x030 - 0x06F)
│       ├── gold                  0x030 - 0x03F
│       ├── alternative           0x040 - 0x04F
│       ├── base                  0x050 - 0x05F
│       └── variant               0x060 - 0x06F
│       
│   
└── MODIFICATION                ((0x600 - 0x93F))
    ├── Edition                  (0x600 - 0x6FF)
    │   └── edition               0x600 - 0x6FF
    │   
    ├── Revision                 (0x700 - 0x7FF)
    │   └── revision              0x700 - 0x7FF
    │   
    ├── Adaption                 (0x800 - 0x86F)
    │   ├── *reserved*            0x800 - 0x80F
    │   ├── focus                 0x810 - 0x81F
    │   ├── style                 0x820 - 0x82F
    │   ├── prospective           0x830 - 0x83F
    │   ├── context               0x840 - 0x84F
    │   ├── action                0x850 - 0x85F
    │   └── edit                  0x860 - 0x86F
    │   
    ├── Transformation           (0x870 - 0x8DF)
    │   ├── *reserved*            0x870 - 0x87F
    │   ├── contrast              0x880 - 0x88F
    │   ├── colour                0x890 - 0x89F
    │   ├── aspect                0x8A0 - 0x8AF
    │   └── size                  0x8B0 - 0x8DF
    │   
    ├── Format                   (0x8E0 - 0x92F)
    │   ├── *reserved*            0x8E0 - 0x8EF
    │   ├── image_format          0x8F0 - 0x8FF
    │   ├── colour_space          0x900 - 0x90F
    │   ├── channel_depth         0x910 - 0x91F
    │   └── compress              0x920 - 0x92F
    │   
    └── Embedded                 (0x930 - 0x93F)
        └── embedded              0x930 - 0x93F
        

```

Extension must be `tif` for images. We are not going to use `tiff`.

## Image folder structure

We are going to use a simple 2-level mapping for the folder structure. The first level is the ARTWORK_ID and the second level is the PURPOSE_CODE.

```text
data/
├── 000001
│   ├── 32 (gold images)
│   │   └── 000001-32.600.2.tif
│   └── 52 (base images)
│   │   └── 000001-52.600.2.tif
└── README.md
```
