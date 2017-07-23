import matplotlib.gridspec as gridspec
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
from tickerFormatter import DateFormatter
import numpy as np

def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x*1e-6)

def bbands(price, length=30, numsd=2):
    """ returns average, upper band, and lower band"""
    ave = price.rolling(window=length).mean()
    sd = price.rolling(window=length).std()
    upband = ave + (sd*numsd)
    dnband = ave - (sd*numsd)
    return np.round(ave,3), np.round(upband,3), np.round(dnband,3)

def plot_price_volume(df, skip_weekends=True, bollinger=True):
    df = df.sort_values('Date')
    df = df.reset_index()
    fig = plt.figure(figsize=(14, 7))
    gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[3, 1])

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[1, 0], sharex=ax0)
    for ax in [ax0, ax1]:
        ax.spines["top"].set_visible(False)
        # ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    price_series = [(df.Close,'price')]

    if bollinger:
        ave, upper, lower = bbands( df.Close )
        price_series = price_series + [ (ave,'moving avg'), (upper,'upper'), (lower,'lower')]

    ax1.yaxis.set_major_formatter(FuncFormatter(millions))
    if not skip_weekends:
        for (s,l) in price_series:
            line_type = '--' if l in ['upper', 'lower'] else '-'
            ax0.plot(df.Date.values, s, line_type, label=l)
        ax1.bar(df.Date.values, df.Volume, color='green', edgecolor='green')
    else:
        N = df.shape[0]
        dateFormatter = DateFormatter(df.Date)
        ind = np.arange(N)
        ax0.xaxis.set_major_formatter(dateFormatter)
        for (s,l) in price_series:
            line_type = '--' if l in ['upper', 'lower'] else '-'
            ax0.plot(ind, s, line_type, label=l)
        ax1.bar(ind, df.Volume, edgecolor='green', color='green')
    ax0.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    fig.autofmt_xdate()


#plot_price_volume(vnm[vnm.Date > datetime.datetime(2017, 1, 1)], skip_weekends=True)