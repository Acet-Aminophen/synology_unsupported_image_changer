# Did you ever know The synology doesn't support webp or jfif? because I just got it.
- This Docker Image changes every webp and jfjf files to png type. if the webp picture is animated, it will be gonna changed to gif.
- You must set volume destination as "/target" in the container.
- Every originl image gonna be backed up in "/target/.before_changed" + original directory path
- It is made for The Synology system. so It ignores "@eaDir" Directory.
- Thanks.
