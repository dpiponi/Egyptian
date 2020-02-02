import sys

file = sys.stdin

print """
\\documentclass[]{article} 
\\usepackage{vmargin}
\\usepackage{hiero}
\\usepackage{egypto}
\\usepackage{scalefnt}
\\setpapersize{custom}{51mm}{34mm}
%\\setpapersize[landscape]{A8} 
\\setmargnohfrb{5mm}{5mm}{5mm}{5mm}  
% l,t,r,b 
\\pagestyle{empty} 
\\setlength{\\pdfpagewidth}{\\paperwidth} 
\\setlength{\\pdfpageheight}{\\paperheight} 
\\begin{document}"""

while True:
    mdc = file.readline().rstrip()
    if not mdc:
        break
    xlat = file.readline().rstrip()
    xlit = file.readline().rstrip()

    print """ \\newpage
\\vspace*{\\fill}
\\begin{center}
\\framebox[1.1\\width]{
\\begin{hieroglyph}
%s
\\end{hieroglyph}
}
\\end{center}
\\vspace*{\\fill}

\\newpage
\\vspace*{\\fill}
\\begin{center}
\\EcritTraductionEnLigne{
%s
}{
%s
}
\\end{center}
\\vspace*{\\fill}""" % (mdc,xlit,xlat)

print """
\\end{document}"""
