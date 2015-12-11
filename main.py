# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:36:23 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fac

# Change mathtext to follow text regular size
plt.rcParams['mathtext.default'] = 'regular'

# Change all fonts to certain size unless otherwise stated
font = {'size' : 14}
plt.rc('font', **font)


'''
Sources
https://da.wikipedia.org/wiki/Lotto_(Danske_Spil)
https://www.lottostat.dk/hvad_er_chancen_for_at_vinde_i_onsdags_lotto.lotto_faq
http://www.mathsisfun.com/data/lottery.html
'''


def find_nearest_ind(array, value):
    near_search = np.abs(array-value)
    idx = (near_search).argmin()
    return idx


def simpleaxis(ax):
    color = 'black'
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_edgecolor(color)
    ax.tick_params(color=color, labelcolor=color)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines['left'].set_zorder(200)
    ax.spines['bottom'].set_zorder(200)


if __name__ == '__main__':

    '''
    Onsdags lotto
    '''

    g = 48
    extra = 6
    g_end = g-extra
    tickets_per_week = 1  # 0000

    '''
    Calc
    '''

    chance_num = fac(g)/(fac(g_end) * fac(extra))
    chance = 1 - tickets_per_week/chance_num

    print '1 in ' + str(int(chance_num)) + ' chance of winning if playing once.'
    print
    print 'Chance to win after 1 week',
    print str(100*(1-chance)) + ' %'
    print
    print 'Chance to win after 50 years'
    print str(100*(1-(chance**2600))) + ' %'
    print
    print 'Chance to win after 1 mio. years'
    print str(100*(1-(chance**(1000000*52)))) + ' %'
    print
    print '25 % chance of winning after playing for',

    '''
    Calculate the probability as a function of weeks played
    '''

    # Say we play once a week for 1 mio. years (52 weeks in a year)
    years = 1000000
    year_all = np.arange(years)
    win_chance = np.empty(years)

    win_chance = 100*(1-(chance**(year_all*52)))

    print str(find_nearest_ind(win_chance,25)) + ' years'

    # If we play 10000 lottery tickets per week we will reach 25% chance of winning
    # after 8 years.
    # We now assume every ticket (in Denmark) costs around 7 dollars

    ticket_price = 7 # 50 dkk or 7 dollars
    total_price = 7*52*10000*ticket_price
    prize = 0.73*10**6#5 M dkk, 0.73 M dollars

    # If we imagine that we win when we hit these 25% and the prize money is
    # 5 M dkk or 3.65 M dollars then the total "winnings" will be

    print 'Prize - price of lottery tickets = ' + str(prize - total_price)
    print 'I.e. we lost ' + str(round((-(prize - total_price))/1000000,1)) + ' M dollars.'

    '''
    Plot
    '''

    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(win_chance, color = '#be0000', lw=3, zorder=100)
    ax.set_title('Why you should not play the lottery')
    ax.set_xlabel('Time played [years]')
    ax.set_ylabel('Chance of winning [%]')
    simpleaxis(ax)
    plt.tight_layout()
    plt.savefig('lottery.png', dpi=400)
    plt.show()
