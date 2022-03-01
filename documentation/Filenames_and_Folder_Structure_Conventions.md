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
000001.42.600.2.tif
```

That is the original (no transformation) base image from artwork with ID 000001.

Artwork ID: manually assigned between 000000 and 999999 for drawings.

Purpose Code:
| Code | Desc          |
|------|---------------|
| 30   | gold index    |
| 31   | gold metadata |
| 32   | gold image    |
| 40   | base index    |
| 41   | base metadata |
| 42   | base image    |

Transformation Code:
| Code | Desc     |
|------|----------|
| 600  | original |

Type Code:
| Code | Desc     |
|------|----------|
| 0    | index    |
| 1    | metadata |
| 2    | image    |

Extension must be `tif` for images. We are not going to use `tiff`.

## Image folder structure

We are going to use a simple 2-level mapping for the folder structure. The first level is the ARTWORK_ID and the second level is the PURPOSE_CODE.

```text
data/
├── 000001
│   ├── 32 (gold images)
│   │   └── 000001-32.600.2.tif
│   └── 42 (base images)
│   │   └── 000001-42.600.2.tif
└── README.md
```
