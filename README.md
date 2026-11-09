# Awesome Data Recovery

A curated list of **free and open-source tools and guides** for getting back deleted photos, videos and files from computers, SD cards, USB drives and Android phones.

Every entry says what the tool is for and what it cannot do. Links were checked when they were added; broken links are reported automatically every month.

## First, the rules that decide whether recovery works

1. **Stop using the device.** Deleted data stays until something overwrites it.
2. **Never save recovered files onto the drive you are recovering from.**
3. **Check the easy places first:** Recycle Bin, phone gallery trash (`Bin`/`Trash`, kept 30-60 days), cloud trash (Google Photos, OneDrive), backups.
4. **Failing drive (clicking, disappearing, read errors)?** Make an image of it first (see [Disk imaging](#disk-imaging)) and recover from the image.
5. **SSDs and most modern phones** erase deleted data quickly (TRIM) or encrypt internal storage, so deep recovery there is often impossible. SD cards, USB sticks and hard disks are the good cases.

## Contents

- [All-in-one recovery tools](#all-in-one-recovery-tools)
- [File carving](#file-carving-recover-by-content-without-file-names)
- [Undelete by file system](#undelete-by-file-system-keeps-names-and-folders)
- [Disk imaging](#disk-imaging)
- [Android](#android)
- [Forensic suites](#forensic-suites)
- [File system documentation](#file-system-documentation)
- [Contributing](#contributing)

## All-in-one recovery tools

- [File Rescue](https://github.com/Bhushansavande/file-rescue) - Windows/Linux/Android. Carves 40+ formats (photos, video, music, documents, databases) and undeletes with original names on FAT32, exFAT, NTFS and ext4. Has a simple window for non-technical users, HTML report, duplicate removal, scan resume. MIT.
- [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec) - the classic carving tool, about 300 file families (480+ extensions), Windows/Linux/macOS, text-mode interface. Ignores the file system, so it also works on damaged or formatted drives, but file names are lost. GPL.
- [TestDisk](https://www.cgsecurity.org/testdisk_doc/) - companion to PhotoRec: repairs lost partitions and boot sectors, and can undelete files on several file systems. Text-mode interface. GPL.
- [Windows File Recovery](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-file-recovery) - Microsoft's command-line tool (`winfr`) from the Microsoft Store, for NTFS and also FAT/exFAT/ReFS in different modes. Free but not open source.

## File carving (recover by content, without file names)

Carving looks for the start of known file types in raw data. It works on formatted or damaged drives but cannot know names or folders, and may return partial files when a file was stored in pieces.

- [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec) - see above.
- [Foremost](https://foremost.sourceforge.net/) - original command-line carver from US Air Force investigators, config-file driven. Older, but still packaged in many distributions.
- [Scalpel](https://github.com/sleuthkit/scalpel) - fast carver derived from Foremost, now under the Sleuth Kit organization.
- [Magic Rescue](https://github.com/jbj/magicrescue) - carver using "recipes" per file type; good for a few specific formats.

## Undelete by file system (keeps names and folders)

- [extundelete](https://extundelete.sourceforge.net/) - ext3/ext4 undelete through the journal. Unmaintained; works best right after deletion.
- [ext4magic](https://ext4magic.sourceforge.net/ext4magic_en.html) - recovers deleted files on ext3/ext4 using journal information, with time filters.
- [TestDisk](https://www.cgsecurity.org/testdisk_doc/) - undelete on FAT, exFAT, NTFS and ext2.
- [File Rescue](https://github.com/Bhushansavande/file-rescue) - FAT32, exFAT, NTFS and ext4 (via the journal), with a plain-language report of which files are intact or overwritten.

## Disk imaging

Recover from a copy, not from the failing original.

- [GNU ddrescue](https://www.gnu.org/software/ddrescue/manual/ddrescue_manual.html) - copies a failing drive while skipping bad areas first and retrying later; the map file lets you stop and resume. The standard choice for damaged media. GPL.

## Android

- **Trash first.** Gallery/Photos *Bin* and the Files app *Recycle bin*; Android 11+ also keeps `.trashed-*` files for about 30 days.
- [File Rescue for Android](https://github.com/Bhushansavande/file-rescue/blob/main/docs/ANDROID.md) - finds trashed files, WhatsApp statuses and thumbnails without root and with no internet permission.
- [DiskDigger](https://diskdigger.org/) - Android and Windows photo recovery; the free version has limits and deep scans on Android need a rooted phone. Not open source.
- **SD card in the phone?** Remove it and scan it from a computer with PhotoRec or File Rescue; that gives far better results than any on-phone app.

## Forensic suites

For people who want to go deeper than recovery.

- [The Sleuth Kit](https://sleuthkit.org/) - command-line library and tools to analyze disk images and file systems, list deleted files and extract them (`fls`, `icat`, `tsk_recover`).
- [Autopsy](https://autopsy.com/) - graphical interface on top of The Sleuth Kit for Windows. Open source.
- [bulk_extractor](https://github.com/simsong/bulk_extractor) - scans raw data for e-mail addresses, URLs, credit-card-like numbers and other features without parsing the file system.

## File system documentation

Understanding how deletion works helps you choose the right tool.

- [ext4 on-disk format (kernel documentation)](https://docs.kernel.org/filesystems/ext4/about.html) - why ext4 erases a deleted file's block list and how the journal can help.
- [exFAT (OSDev wiki)](https://wiki.osdev.org/ExFAT) - overview of the exFAT structures: entry sets, allocation bitmap, no-FAT-chain flag.
- [How File Rescue works](https://github.com/Bhushansavande/file-rescue/blob/main/docs/HOW_IT_WORKS.md) - carving versus undelete, in plain language, for FAT, exFAT, NTFS and ext4.

## Contributing

Pull requests are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md). Only free tools and clear guides; no paid "recover everything" products, no affiliate links.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the author has waived all copyright and related rights to this work.
