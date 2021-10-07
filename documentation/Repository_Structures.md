# Repository Structure

↳ For Naming Codes see: [Naming Codes](Naming_Codes.md)  
↳ For Filename Structure see: [Filename Structure](Filename_Structure.md)

---

## Image folder structure

We are going to use a simple 2-level mapping for the folder structure.

1. Concatenated **global library code** and **unicode private art identifier**.

2. The **local index code**.

## Format
```
|REPOSITORY|

    data/

        {GLOBAL_LIBRARY_CODE}{UNICODE_PRIVATE_ART_IDENTIFIER}/

            {LOCAL_INDEX_CODE}/

                {FILE 1}
                {FILE 2}
                {FILE .}
                {FILE N}

    README.md
```

### Example

The list of files (taken from the examples in [Filename Structure Conventions](Filename_Structure_Conventions.md)):

```
aaa100001-00.000.0.json
aaa100001-01.001.1.json
aaa100001-30.000.0.json
aaa100001-31.001.1.json
aaa100001-32.600.700.1.json
aaa100001-32.600.700.2.tif
aaa100001-33.810.42.600.1.json
aaa100001-33.810.42.600.2.tif
aaa100001-40.000.0.json
aaa100001-41.001.1.json
aaa100001-42.32.600.700.1.json
aaa100001-42.32.600.700.2.tif
aaa100001-43.33.810.32.600.700.1.json
aaa100001-43.33.810.32.600.700.1.tif
aaa100001-50.000.0.json
aaa100001-51.001.1.json
aaa100001-52.32.600.700.1.json
aaa100001-52.32.600.700.2.tif
aaa100001-53.33.810.32.600.700.1.json
aaa100001-53.33.810.32.600.700.1.tif
aaa100001-60.000.0.json
aaa100001-61.001.1.json
aaa100001-62.920.42.32.600.700.1.json
aaa100001-62.920.42.32.600.700.2.tif
aaa100001-63.920.43.33.810.32.600.700.1.json
aaa100001-63.920.43.33.810.32.600.700.1.tif
```

Will produce the the folder structure:

```
data/
├── aaa100001/
│   ├── aaa100001-00.000.0.json
│   ├── aaa100001-01.001.1.json
│   ├── 30/
│   │   ├── aaa100001-30.000.0.json
│   │   ├── aaa100001-31.001.1.json
│   │   ├── aaa100001-32.600.700.1.json
│   │   ├── aaa100001-32.600.700.2.tif
│   │   ├── aaa100001-33.810.42.600.1.json
│   │   └── aaa100001-33.810.42.600.2.tif
│   ├── 40
│   │   ├── aaa100001-40.000.0.json
│   │   ├── aaa100001-41.001.1.json
│   │   ├── aaa100001-42.32.600.700.1.json
│   │   ├── aaa100001-42.32.600.700.2.tif
│   │   ├── aaa100001-43.33.810.32.600.700.1.json
│   │   ├── aaa100001-43.33.810.32.600.700.1.tif
│   ├── 50
│   │   ├── aaa100001-50.000.0.json
│   │   ├── aaa100001-51.001.1.json
│   │   ├── aaa100001-52.32.600.700.1.json
│   │   ├── aaa100001-52.32.600.700.2.tif
│   │   ├── aaa100001-53.33.810.32.600.700.1.json
│   │   ├── aaa100001-53.33.810.32.600.700.1.tif
│   └── 60
│       ├── aaa100001-60.000.0.json
│       ├── aaa100001-61.001.1.json
│       ├── aaa100001-62.920.42.32.600.700.1.json
│       ├── aaa100001-62.920.42.32.600.700.2.tif
│       ├── aaa100001-63.920.43.33.810.32.600.700.1.json
│       └── aaa100001-63.920.43.33.810.32.600.700.1.tif
└── README.md
```

