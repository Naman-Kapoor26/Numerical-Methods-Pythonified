a
    ??e`?  ?                   @   sd   d dl mZmZ d dlmZmZ d dlmZmZm	Z	m
Z
 dd? Zdd? Zdd	? Zd
d? Zdd? ZdS )?    )?render?HttpResponse)?
Derivative?symbols)?sin?cos?log?pic                 C   s
   t | d?S ?Nz
index.html?r   ??request? r   ?D:\Django\Hi\home\views.py?index   s    r   c                 C   s
   t | d?S )Nz
about.htmlr   r   r   r   r   ?about   s    r   c                 C   s
   t | d?S r
   r   r   r   r   r   ?services   s    r   c                 C   s
   t | d?S )Nzcontact.htmlr   r   r   r   r   ?contact   s    r   c                    s?   t | ?d???dd?}| ?d?}| ?d?}| ?d?}dd? ? td	??? ?fd
d?}|||||?}|d |d |d |d |d d?}t| d|?S )N?
expression?^z**?a?bZnum_decc                 S   s(   | ? d|?}tt|?|? tt|?|?S )N?x)?replace?round?eval)?fun?h?correctZfun_r   r   r   ?funct   s    zN_R.<locals>.functr   c                    s?   i }|| d |dt d? < tdd?D ]?}t|dt |d ?  t? | t |dt |d ?  ?|d ?? t t| ???? ?t |dt |d ?  ?|d ? |d ? |d ?|dt |? < q&|S )N?   r   r   ?   ?   )?str?ranger   r   Zdoit)r   r   r   r   ?d?i?r   r   r   r   ?New_Raph   s
    ?zN_R.<locals>.New_Raph?x1?x2Zx3Zx4Zx5)Znum1Znum2Znum3Znum4Znum5zresullt.html)r#   ?getr   r   r   )r   ?expr   r   Znum_decimalr(   ?Dict?contextr   r'   r   ?N_R   s    


?r/   N)Zdjango.shortcutsr   r   Zsympyr   r   ?mathr   r   r   r	   r   r   r   r   r/   r   r   r   r   ?<module>   s   