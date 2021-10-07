# Naming Codes

↳ For Filename Structure see: [Filename Structure](Filename_Structure.md)  
↳ For Repository Structure see: [Repository Structure](Repository_Structures.md)

---

## Summary

### **There are six different codes that used for naming files:**

1. **Global Library Code**  
Code of the Library where the the Artistic Work is registered.

2. **Unicode Private Art Identifier**  
Private Identifier for each Conceptual Art. Local to Library Namespace.

3. **Type Code**  
A supplement to order the: Index, Metadata, and Media files.

4. **Purpose Code**  
Notes the intended use of the Artistic Work files.

5. **Modification Code**  
Notes the edition, revision, artistic adaption, transformation, format, and embedded metadata of the media files.

6. **File Extension**  
Informal: To guide applications and users of the type type.

### **There are four different code namespaces:**

1. **Global Library Code**  
Three letter code (case insensitive)

2. **Unicode Private Art Identifier**  
Unicode Supplementary Private Use Area-B

3. **Type, Purpose, and Modification Codes**  
Hex-code between 0x000 and 0xFFF.

4. **File Extension**  
Informal: Character String

### Other Meta-Data
*The bulk of the metadata should be included in the dedicated `metadata` files.*

---

## 1. Global Library Code
***(AAA..ZZZ)*** or ***(aaa..zzz)***  
**case insensitive*, prefer lower-case.

*Three Letter Code to uniquely identify the Library of the Artistic Work*

To avoid Namespace Clashes. A Library Code is used note what is the Registration Library of the work.

---

## 2. Unicode Private Art Identifier
Uses unicode plane 16:  
***(U+100000..U+10FFFF)*** except non-characters: **U+10FFFE** and **U+10FFFF**.

Please see: [Unicode 14.0: 23.5. Private-Use Characters: Supplementary Private Use Areas](http://www.unicode.org/versions/Unicode14.0.0/ch23.pdf#G19378)

*Any unicode code point within the Supplementary Private Use Area-B.*

### Notes:

1. The motivation of using character points as the index of the identifiers is so that a font-file could easily be built that shows icon or a emoji style summary of the visual artistic works in a library.

2. In the case that the Library is open for the public to view, it is recommended that through some sort of agreement the libraries choose non-overlapping blocks from the Unicode Plane 16 to use for their identifiers.

2.1 The primary motivation for this recommendation is that a single artistic work may be registered in more than one library without needing to changes its Identifier.

3. Each artistic work concept should be given it's own identifier.

3.1 Editions, Revision, Iterations and Variations of the single art concept should use same identifier.

3.2 When a conceptual change to the fundamental art concept is made, a new identifier should be issued.

---

## 3. Type Code
***(0x000 - 0x00F)***

*Index, Metadata, or Media.*

| Code  | Desc     |
| ----- | -------- |
| 0x000 | index    |
| 0x001 | metadata |
| 0x002 | media    |

---

## 4. Purpose Code
***(0x030 - 0x0FF)***

#### **Gold and Alternative**
(0x030 - 0x03F)  
*created by artists*.

| Code  | Description                          |
| ----- | ------------------------------------ |
| 0x030 | gold and alternative local index     |
| 0x031 | gold and alternative common metadata |
| 0x032 | gold                                 |
| 0x033 | alternative                          |

---

#### **Acquired**
(0x040..0x04F)  
*scanned by artists, recored by artists, other source material*.

| Code  | Description          |
| ----- | -------------------- |
| 0x040 | acquired local index |
| 0x041 | acquired metadata    |
| 0x042 | acquired media       |

---

#### **Base**
(0x050 - 0x05F)  
Gold > *Processed (base specification)* > Base  
*automatically generated*.

| Code  | Description             |
| ----- | ----------------------- |
| 0x050 | base local index        |
| 0x051 | base common metadata    |
| 0x052 | base                    |
| 0x053 | base alternative        |

---

#### **Variant**
(0x060 - 0x06F)  
Base > *Processed (various transformations)* > Variant  
*automatically generated*.

| Code  | Description                |
| ----- | -------------------------- |
| 0x060 | variant local index        |
| 0x061 | variant common metadata    |
| 0x062 | variant                    |
| 0x063 | variant alternative        |

---

## 5. Modification Code
***(0x600 - 0xFFF)***

#### **Editions**
*created by artists*  
0x600 - 0x6FF  
(full code block)

The editions of a artistic work.

| Code  | Description                     |
| ----- | ------------------------------- |
|       | ***0x600 - 0x6FF***             |
| 0x600 | edition #001                    |
| 0x601 | edition #002                    |
| 0x601 | edition #003                    |
| 0x6.. | edition #...                    |
| 0x6.. | edition #...                    |
| 0x6FE | edition #255                    |
| 0x6FF | edition #256                    |

---

#### **Revision**
*created by artists*  
0x700 - 0x7FF  
(full code block)

The revision of a artistic work.

| Code  | Description                     |
| ----- | ------------------------------- |
|       | ***0x700 - 0x7FF***             |
| 0x700 | revision #001                   |
| 0x701 | revision #002                   |
| 0x702 | revision #003                   |
| 0x7.. | revision #...                   |
| 0x7.. | revision #...                   |
| 0x7FE | revision #255                   |
| 0x7FF | revision #256                   |

---

#### **Artistic Adaption**
*created by artists*  
0x800 - 0x8FF  
(code block)

| Code  | Description                     |
| ----- | ------------------------------- |
|       | ***0x810 - 0x81F***             |
| 0x810 | (focus) background              |
| 0x811 | (focus) background blur         |
| 0x812 | (focus) background transparent  |
| 0x813 | (focus) foreground              |
| 0x814 | (focus) foreground blur         |
| 0x815 | (focus) foreground transparent  |
| 0x816 | (focus) wash                    |
|       |                                 |
|       | ***0x820 - 0x82F***             |
| 0x820 | (style) cartoon                 |
| 0x821 | (style) outline                 |
| 0x822 | (style) line-art                |
| 0x823 | (style) charcoal                |
|       |                                 |
|       | ***0x830 - 0x83F***             |
| 0x831 | (prospective) tall              |
| 0x832 | (prospective) wide              |
| 0x833 | (prospective) prospective       |
| 0x834 | (prospective) wide-angle        |
| 0x835 | (prospective) macro             |
| 0x836 | (prospective) top               |
| 0x837 | (prospective) bottom            |
| 0x838 | (prospective) left              |
| 0x839 | (prospective) right             |
| 0x83A | (prospective) inside            |
| 0x83B | (prospective) outside           |
|       |                                 |
|       | ***0x840 - 0x84F***             |
| 0x840 | (context) day                   |
| 0x841 | (context) night                 |
| 0x842 | (context) windy                 |
| 0x843 | (context) hot                   |
| 0x844 | (context) underwater            |
|       |                                 |
|       | ***0x850 - 0x85F***             |
| 0x840 | (action) sleeping               |
| 0x841 | (action) running                |
| 0x842 | (action) eating                 |
| 0x843 | (action) dancing                |
|       |                                 |
|       | ***0x860 - 0x86F***             |
| 0x860 | (edit) loud                     |
| 0x861 | (edit) quite                    |
| 0x862 | (edit) looping                  |
| 0x863 | (edit) dynamic                  |
| 0x864 | (edit) soft                     |
| 0x865 | (edit) aggressive               |

---

#### **Transformation**
*automatically generated*
0x900 - 0x9FF  
(code block)

| Code  | Description                     |
| ----- | ------------------------------- |
|       | ***0x910 - 0x91F***             |
| 0x910 | (contrast) low                  |
| 0x911 | (contrast) medium               |
| 0x912 | (contrast) high                 |
| 0x913 | (contrast) extreme              |
|       |                                 |
|       | ***0x920 - 0x92F***             |
| 0x920 | (colour) back and white         |
| 0x921 | (colour) greyscale              |
| 0x922 | (colour) dull                   |
| 0x923 | (colour) vivid                  |
| 0x924 | (colour) invert                 |
|       |                                 |
|       | ***0x930 - 0x93F***             |
| 0x930 | (aspect) flip vertically        |
| 0x931 | (aspect) flip horizontally      |
| 0x932 | (aspect) rotate left 90         |
| 0x933 | (aspect) rotate right 90        |
| 0x934 | (aspect) double height          |
| 0x935 | (aspect) double width           |
|       |                                 |
|       | ***0x430 - 0x95F***             |
| 0x930 | (size) unchanged                |
| 0x931 | (size) >= 512MP                 |
| 0x932 | (size) <  512MP                 |
| 0x933 | (size) <  50MP                  |
| 0x934 | (size) <  12MP                  |
| 0x935 | (size) <  10MP                  |
| 0x936 | (size) <  8MP                   |
| 0x937 | (size) <  6MP                   |
| 0x938 | (size) <  5MP                   |
| 0x939 | (size) <  4MP                   |
| 0x93A | (size) <  3MP                   |
| 0x93B | (size) <  2MP                   |
| 0x93C | (size) <  1MP                   |
| 0x93D | (size) <  0.9MP                 |
| 0x93E | (size) <  0.8MP                 |
| 0x93F | (size) <  0.7MP                 |
| 0x940 | (size) <  0.6MP                 |
| 0x941 | (size) <  0.5MP                 |
| 0x942 | (size) <  0.4MP                 |
| 0x943 | (size) <  0.3MP                 |
| 0x944 | (size) <  0.25MP                |
| 0x945 | (size) <  0.2MP                 |
| 0x946 | (size) <  0.18MP                |
| 0x947 | (size) <  0.16MP                |
| 0x948 | (size) <  0.15MP                |
| 0x949 | (size) <  0.14MP                |
| 0x94A | (size) <  0.13MP                |
| 0x94B | (size) <  0.12MP                |
| 0x94C | (size) <  0.11MP                |
| 0x94D | (size) <  0.10MP                |
| 0x94E | (size) <  0.09MP                |
| 0x94F | (size) <  0.08MP                |
| 0x950 | (size) <  0.07MP                |
| 0x951 | (size) <  0.06MP                |
| 0x952 | (size) <  0.05MP                |
| 0x953 | (size) <  0.04MP                |
| 0x954 | (size) <  0.03MP                |
| 0x955 | (size) <  0.02MP                |
| 0x956 | (size) <  0.01MP                |
| 0x957 | (size) <  0.009MP               |
| 0x958 | (size) <  0.008MP               |
| 0x959 | (size) <  0.007MP               |
| 0x95A | (size) <  0.006MP               |
| 0x95B | (size) <  0.005MP               |
| 0x95C | (size) <  0.004MP               |
| 0x95D | (size) <  0.003MP               |
| 0x95E | (size) <  0.002MP               |
| 0x95F | (size) <  0.001MP               |

---

#### **Format**
*automatically generated*
0xA00 - 0xAFF  
(code block)

| Code  | Description                     |
| ----- | ------------------------------- |
|       | ***0xA00 - 0xA0F***             |
| 0xA00 | (image format) tiff             |
| 0xA01 | (image format) jpeg             |
| 0xA02 | (image format) png              |
|       |                                 |
|       | ***0xA10 - 0xA1F***             |
| 0xA10 | (colour space) sRGB             |
| 0xA11 | (colour space) AdobeRGB         |
| 0xA12 | (colour space) P3               |
|       |                                 |
|       | ***0xA20 - 0xA2F***             |
| 0xA21 | (channel depth) 8bit            |
| 0xA22 | (channel depth) 10bit           |
| 0xA23 | (channel depth) 12bit           |
| 0xA24 | (channel depth) 14bit           |
| 0xA25 | (channel depth) 16bit           |
| 0xA26 | (channel depth) 24bit           |
| 0xA27 | (channel depth) 32bit           |
| 0xA28 | (channel depth) 64bit           |
|       |                                 |
|       | ***0xA30 - 0xA3F***             |
| 0xA30 | (compress) uncompressed         |
| 0xA31 | (compress) lossless             |
| 0xA32 | (compress) transparent          |
| 0xA33 | (compress) excellent            |
| 0xA34 | (compress) great                |
| 0xA35 | (compress) very good            |
| 0xA36 | (compress) good                 |
| 0xA37 | (compress) poor                 |
| 0xA38 | (compress) very poor            |
| 0xA39 | (compress) worst                |

---

#### **Embedded Metadata**
*automatically generated*
0xE00 - 0xEFF  
(code block)

| Code  | Description                     |
| ----- | ------------------------------- |
|       | ***0xE10 - 0xE1F***             |
| 0xE10 | unmodified                      |
| 0xE11 | blank                           |
| 0xE12 | copyright only                  |
| 0xE13 | copyright and artist            |
| 0xE14 | full                            |

---

## 6. File Extension

Prefixed with a period, this is the last part of the file name.
Informally guide applications and users of the type type.

### Some Examples:
| Extension  | Type          |
| ---------- | ------------- |
| .json      | JSON Text     |
| .tif       | TIFF Image    |
| .flac      | FLAC Audio    |
