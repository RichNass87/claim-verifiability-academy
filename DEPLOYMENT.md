# Deployment Guide

This guide launches the package on GitHub, Hugging Face Spaces, Zenodo, and Academia.edu.

## 1. GitHub repository

Suggested repository name: `claim-verifiability-academy`

```bash
git init
git add .
git commit -m "Initial Claim Verifiability Academy launch package"
git branch -M main
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/claim-verifiability-academy.git
git push -u origin main
```

Before pushing publicly, update:

- `CITATION.cff` repository URL
- `.zenodo.json` creator/license metadata
- `LICENSE`
- Any proprietary source materials you do not want public

## 2. Hugging Face Space

1. Create a new Space.
2. Choose SDK: Gradio.
3. Copy the contents of `space/` into the Space repository root.
4. The Space should contain `README.md`, `app.py`, and `requirements.txt`.
5. Commit the files. The Space runtime will install requirements and run `app.py`.

## 3. Zenodo DOI

Option A - GitHub integration:

1. Connect Zenodo to GitHub.
2. Enable the `claim-verifiability-academy` repository in Zenodo.
3. Create a GitHub release, for example `v0.1.0`.
4. Zenodo archives the release and issues a DOI.
5. Replace placeholder DOI fields in the README, paper, and `CITATION.cff` if desired.

Option B - manual upload:

1. Zip this repository.
2. Upload the ZIP to Zenodo as software.
3. Use the metadata from `.zenodo.json`.
4. Add the working paper PDF as an additional file if you want the paper and software archived together.

## 4. Academia.edu

Upload `paper/claim_verifiability_working_paper.pdf` and use `paper/academia_metadata.md` for the title, abstract, tags, and summary.

## 5. Suggested release checklist

- [ ] Confirm author and organization names.
- [ ] Confirm whether Claim Verifiability(TM) and Inspector Roofing Protocols(TM) should be public, private, or split-licensed.
- [ ] Replace `YOUR-GITHUB-USERNAME` placeholders.
- [ ] Create GitHub repo.
- [ ] Create Hugging Face Space.
- [ ] Make release `v0.1.0`.
- [ ] Mint DOI on Zenodo.
- [ ] Upload paper PDF to Academia.
