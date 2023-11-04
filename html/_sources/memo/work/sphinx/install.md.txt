# Sphinxの導入とGitHubページの作成

## Sphinxのインストール
[公式ページ](https://www.sphinx-doc.org/ja/master/usage/installation.html#windows)を参考にSphinxをインストールする

## Spinx Project の作成
1. sphinx-quickstartコマンドでプロジェクトを作成する。
```bash
sphinx-quickstart
```

以下の要領で設定を行う
```
Welcome to the Sphinx 7.2.6 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: debug record
> Author name(s): org.debugrecord
> Project release []: 0.1-SNAPSHOTS

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: ja

Creating file XXXXX\debugrecord\docs\source\conf.py.
Creating file XXXXX\debugrecord\docs\source\index.rst.
Creating file XXXXX\debugrecord\docs\Makefile.
Creating file XXXXX\debugrecord\docs\make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file XXXXX\debugrecord\docs\source\index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

2. 拡張テーマの適用のため、conf.pyに以下を追記・書き換えする。 
```python
import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

3. MarkDown形式のファイルを利用可能にするため、conf.pyに以下を追記・書き換えする。 
```python
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

```

4. Githubページへの適用のため、ビルドのディレクトリ構成を変更する。
Windowsを利用しているため、make.batに以下の設定を追記・書き換え
```bash
set BUILDDIR=.
set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% source
set I18NSPHINXOPTS=%SPHINXOPTS% source


if "%1" == "html" (
	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%.
	goto end
)

```

## GitHub Pageの作成
1. Github上でレポジトリ(doc)を作成した後、masterと gh-pagesという名前のブランチを作成する
```bash
git clone https://github.com/debugrecord/docs.git
cd doc
git branch master
git branch gh-pages
```

2. 作成したgh-pagesブランチに切り替え、sphinxsプロジェクトコピーし、htmlでビルドする。(index.htmlがルートに来るようにする。)
```bash
git checkout gh-pages
cp somepath/test_sphinx .
make html
```

3. ビルドして出来たHTMLをプッシュし、http://xxxxxx.github.io/projectへアクセスする。
```bash
git push origin gh-pages
```