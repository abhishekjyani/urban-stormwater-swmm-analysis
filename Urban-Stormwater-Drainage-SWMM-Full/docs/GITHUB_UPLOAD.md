# Uploading this project to GitHub

## Recommended repository name

`Urban-Stormwater-Drainage-SWMM`

## GitHub web upload

1. Sign in to GitHub and create a new **public** repository.
2. Name it `Urban-Stormwater-Drainage-SWMM`.
3. Do not initialize it with another README if you are uploading this package as-is.
4. Extract the ZIP package.
5. Upload the **contents inside** the `Urban-Stormwater-Drainage-SWMM-Full` folder, not the outer ZIP itself.
6. Commit the files.
7. Confirm that `README.md` renders and that the figures appear correctly.

## Git command-line alternative

```bash
git init
git add .
git commit -m "Initial SWMM urban drainage project"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

## Before sharing

Check that:

- all `.inp` files open in EPA SWMM 5.2,
- the technical report opens,
- figures render in the README,
- no personal/private files were accidentally added,
- the repository is public if it is intended for external verification.
