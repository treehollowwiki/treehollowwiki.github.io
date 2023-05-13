# 用于生成帖子模版的脚本

#!/usr/bin/python
# -*- coding: utf-8 -*-

from encodings import utf_8
import time

title_time = time.strftime("%Y-%m-%d",time.localtime())
title_txt = input("标题:")
title_str = title_time + "-"+title_txt.replace(" ","-")+".md"

md_doc = open(title_str,'a',encoding='utf-8')
md_doc.write("---\n")
md_doc.write("layout: git-wiki-post\n")
md_doc.write("title: "+title_txt+"\n")
author = input("原帖作者学校：")
md_doc.write(f"author: 来自{author}的洞友 \n")
date = time.strftime("%Y-%m-%d %H:%M",time.localtime())
md_doc.write("date: "+date+"+0800\n")
md_doc.write("---\n")

md_doc.write("\n\n")
md_doc.write(f"# {title_txt}\n")
md_doc.write("请将这段内容替换为你的内容的的简介，也可以是文章的第一段，但是内容不要过长。\n\n")

md_doc.write("请在这里开始书写你的内容\n")