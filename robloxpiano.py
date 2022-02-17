import keyboard
from time import sleep

song_text="""
w r w r w r w r Q e Q e Q e Q e 0 y 0 y 0 y 0 y 8 w 8 w 8 t 8 r w r w r w r w r Q e Q e Q r Q w 8 w 8 w 8 w 8 w 8 w 8 w 8 w 8 w 8 r w [ra] [wa] r [ws] [rd] Q e Q [se] [aQ] e [sQ] [ed] 0 r 0 [sr] [a0] r [s0] [rd] 8 w [s8] [wu] 8 t [s8] [ra] w r w r w [ro] [wp] [ra] Q e Q e [dQ] y 8 w [f8] w 8 w 8 w 8 w 8 w 8 w 8 t 8 r w r w r [wa] r [ws] [rd] Q e Q e [aQ] e [sQ] [ed] 0 r 0 r [a0] r [s0] [rd] 8 [wf] 8 [wu] 8 t [s8] [ra] w r w r w [ro] [wp] [ra] Q e Q e [pQ] y Q w [o8] w 8 w 8 w 8 w 8 w 8 w 8 w 8 w 9 e [p9] [pe] [p9] e [p9] [pe] [a0] r [a0] [ra] [p7] Q [o7] [uQ] 8 w [o8] w 8 w 8 w 8 w [t8] w 8 [wto] 8 w [yp9] e [p9] [pe] [p9] e [p9] [pe] [a0] r [a0] [ra] [p7] Q [o7] [oQ] 8 w 8 w 8 w 8 w [t8] w 8 w [to8] w 8 w 2 6 [yp2] [yp6] [yp2] 6 [o2] [p6] [ua3] 7 [ua3] [ua7] [p7] $ [o7] [u$] 1 5 [o1] 5 1 5 [t1] 5 1 5 1 5 1 [w5] 1 5 2 6 [yd2] [yd6] [yd2] 6 [ya2] [ya6] [ys3] 7 [ya3] 7 [yp7] $ [o7] [o$] 1 5 8 0 w t u o [sh] f [of5] [ohd] [ohd] w p [wpjd] [pjd] w a [wkda] w 9 d [rpd9] 9 [pdG] [pdG] [pG9] [ohd] 9 [ohd] 9 [pjdG] 9 [pjdG] 9 [9$] o [sl6] [kea] [ka] e [pje] [pj] e [ohe] [oh] e [pj0] [uf] 1 5 8 0 w t [wu] [o0] [us8] 6 3 5 [soh8] 5 3 [od] [od5] o [ohd9] [wohd] 9 e [pjd9] [wpjd] 5 9 [wkda] [kda9] r 9 7 d [pd2] 6 [pG9] [pG6] 0 [phd6] [phd9] 6 2 [pjd6] 9 [pjd6] 9 $ 9 [o6] p [sl] 0 [kea] [ka0] r 0 [pje] [pj0] 6 0 [ohe] [oh0] r 0 [pj6] [oh1] 5 8 0 w t u o [sf] a d [wtf8] d d a d f d s a a w r w r w r w r Q e Q e Q e Q e 0 y 0 y 0 y 0 y 8 w 8 w 8 t 8 r w r w r [wa] r [ws] [rd] Q e Q e [aQ] e [sQ] [ed] 0 y 0 y [a0] y [s0] [yd] 8 [wf] 8 [wf] 8 t [s8] [ra] w r w r w r w [ra] [aQ] e [pQ] e [sQ] y Q w 8 w [a8] [wo] 8 w [I8] w [o8] w 8 w [sl8] t 8 r [wka] r w r [wa] r [ws] [rd] Q e Q e [aQ] e [sQ] [ed] 0 y 0 y [h0] y [G0] [yf] 8 [wd] 8 [wu] 8 [ts] 8 [ra] w r w r w r [wo] [rp] [aQ] e Q e [pQ] y Q w [s8] w 8 w [to8] w 8 w [to8] w 8 w [to8] w 8 w [yp2] 6 [yp9] [yp0] [ywp] o p [ua3] 7 [ua0] [ua] [yp7] [o7] u 1 5 8 0 w t w t w t w [to] w t 0 [yp2] 6 [yp9] [yp0] [ypQ] o p [ua3] 7 [ua0] [ua] [p7] 7 a [o1] 5 8 0 w t o s f w [hd] t [dG] w [pdI] 8 [ypI] 6 [yp9] [yp0] [ypQ] o p [ua3] [73] [d0] f [a7] r o u 1 [o5] 8 0 w t u o w y w [wso] [y0] y 2 6 [yd9] [ydQ] [yd9] 6 [p3] a [s3] 7 [a0] p 7 7 o [od1] [f5] 8 0 w [to] s [oh1] 1 1 2 [d5] 9 [wha] [rha] w 9 [wjda] [jda9] 5 9 [wkda] [rkda] w 9 [d7] [pd2] 6 [pdG9] Q [pedG] [yhd] e [yhd] e [yjd] e [jed] Q 0 Q [h0] [sl6] 0 [ske] [sk0] r 0 [tsj] [sj0] 6 0 [she] [sh0] 7 0 [sj6] [f1] 5 8 0 w t o s [soh] 5 8 [o5] [sof1] 8 $ [od8] [od5] 9 [wohd] [rohd] w 9 [wpjd] [pjd9] 5 9 [wkda] [rkda] w 9 [d7] [pd2] [pdG6] 9 [pdQG] e y [phed] [yphd] e y [pjed] [ypjd] e Q 0 [o9] [so6] 0 [kfe] [kf0] r 0 [jfe] [jf0] 6 0 [hfe] 0 [hfe] [jf0] [h7] 1 5 8 0 w t u s h a d [tof] d d a a f d s a a [uoa] [uoa] o [upoa] a [uoa] o [oaY] [oaY] o [poaY] a [oaY] o [yoa] [yoa] [yoa] u [yoa] [upaT] [upT] p [upT] [upaT] u 1 5 8 0 w t y d [oG] [oh] [oh] w 5 9 w [ra] [yd] o y r [wa] 9 o [raIG7] [wuroa0] [wr0] o [wrp0] [wra0] o [wr(] [wr(] o [wrp(] [wra(] o [wr9] [wr9] y [ywr9] u [wro9] a [e0] [e0] [pe0] [ea0] u 1 5 8 0 w t [yd] [yd] [pj] [ka] [yd] [d5] 1 5 8 0 w t [soh] [soh] [pj] [oh] [IG] [oh] 5 [skhf1] 5 8 0 w t [sof] [sof] w 0 [woh] 0 [IG9] 0 [oh9] [kf1] 5 8 0 w t [jd] [jd] 2 6 9 0 Q e y u I d [ywod] h h j j k k z [zeQ9] C C v v b b h [wl60] k k j j h h j h [l1] [k1] k 1 h 1 [xh] 1 1 [zh] [zh1] [10] [30] d [d5] o [ohd] [ohd] w p [wpjd] [pjd] w a [wkda] [kda] w 9 7 [d6] [d92] [pdG9] [pdG] 9 [phd] 9 [phd] 9 [phd] 9 [pjdG] 9 [pjdG] 9 $ [o9] [slh6] 0 [ha] [ha] e [pje] [pj] e [ohe] [ohe] [pje] [oh0] 1 5 8 0 w t o s [sof] 8 5 8 5 3 [o2] [s5] [sl81] [ka8] [ka] 8 [oh8] [pj] [sl8] [ka8] 5 [oh81] [pj6] [zd5] 7 [d9] w [kha9] 7 5 9 [zjC$] 9 Q e [zjQ] 9 [jC$] 9 [vkh3] 7 0 w r u r w 1 5 8 0 w t u o s k z [xtso] z z k z x z l k k w r w r w r w r Q e Q e Q e Q e 0 y 0 y 0 y 0 y 8 w t u o s f h l x v m
"""

song_text = song_text.replace('[', "")
song_text = song_text.replace(']', "")
song_text = song_text.replace(" ", "-")
song_text = song_text.replace('\n', ' ')
song_text = song_text.replace('{', '')
song_text = song_text.replace('}', '')

def play_song(string, delay):
    for letterI in range(len(string)):
        try:
            if string[letterI+1] != "-":
                how_many = str(string).find("-", letterI)
                combostr = ""
                for combo in range(letterI, how_many-1):
                    combostr += string[combo]
                keyboard.write(combostr)
            
            if string[letterI] == "-":
                sleep(delay)
           
            elif string[letterI].isupper():
                keyboard.press_and_release("shift+" + string[letterI])
          
            else:
                keyboard.press_and_release(string[letterI])
        except Exception as e:
            print(e)
        else:
            pass

## Initialize #
play_song(song_text, .3)