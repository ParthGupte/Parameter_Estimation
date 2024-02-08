def get_code(img_name):
    latex_code = r"""
            \item """+img_name+r"""\_noise
        \begin{figure}[h]
            \centering
            \includegraphics[width=0.6\textwidth]{images/greyscale/"""+img_name+r""".png}
            \caption{Original Image}
        \end{figure}
        \begin{figure}[h]
            \centering
            \includegraphics[width=0.6\textwidth]{images/outputs/noise/"""+img_name+r"""_noise.png}
            \caption{Recovered Image}
        \end{figure}
        \begin{figure}[h]
            \centering
            \includegraphics[width=1\textwidth]{images/outputs/modelres/"""+img_name+r"""_noise.png}
            \caption{Model Resolution Matrix}
        \end{figure}
        \begin{figure}[h]
            \centering
            \includegraphics[width=1\textwidth]{images/outputs/datares/"""+img_name+r"""_noise.png}
            \caption{Data Resolution Matrix}
        \end{figure}
        \clearpage
    """
    return latex_code

img_names = ["alban-modified","aztec-modified","bee_nest_front_honey-modified","carved_pumpkin-modified","cow","creeper","sheep","skeleton","steve","zombie"]
for img_name in img_names:
    print(get_code(img_name))
