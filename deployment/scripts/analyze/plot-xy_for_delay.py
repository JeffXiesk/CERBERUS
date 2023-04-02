import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


xpoints1 = np.array([1077.583913914631,1074.2716806119781,1077.3878903134778,1101.0019170479911,1196.1392730587565])
ypoints1 = np.array([567.7493007594937,597.6993098455599,578.8585185561769,1006.7967996146435,1543.742856798457])

xpoints2 = np.array([2152.2396462093834,2121.9559695438134,2142.4029941580498,2153.7778968231314,2126.0506667099303])
ypoints2 = np.array([604.0827948523846,640.8506093251534,705.3987701033526,1262.9586553287982,2261.0779678277054])

xpoints3 = np.array([4322.302559003292,4332.696257084505,4347.359571240168,3029.9663003364767])
ypoints3 = np.array([729.5202680594009,731.4199301162645,822.5781797050737,3676.5393862723618])


plt.plot(xpoints1, ypoints1,'-o')
plt.plot(xpoints2, ypoints2,'-o')
plt.plot(xpoints3, ypoints3,'-o')

xline0ms = np.array([1077.583913914631,2152.2396462093834,4322.302559003292])
yline0ms = np.array([567.7493007594937,604.0827948523846,729.5202680594009])

xline100ms = np.array([1074.2716806119781,2121.9559695438134,4332.696257084505])
yline100ms = np.array([597.6993098455599,640.8506093251534,731.4199301162645])

xline200ms = np.array([1077.583913914631,2142.4029941580498,4347.359571240168])
yline200ms = np.array([578.8585185561769,705.3987701033526,822.5781797050737])

xline500ms = np.array([1101.0019170479911,2153.7778968231314,3029.9663003364767])
yline500ms = np.array([1006.7967996146435,1262.9586553287982,3676.5393862723618])

xline1000ms = np.array([1196.1392730587565,2126.0506667099303])
yline1000ms = np.array([1543.742856798457,2261.0779678277054])

plt.plot(xline0ms, yline0ms,'k--',linewidth=0.2)
plt.plot(xline100ms, yline100ms,'k--',linewidth=0.2)
plt.plot(xline200ms, yline200ms,'k--',linewidth=0.2)
plt.plot(xline500ms, yline500ms,'k--',linewidth=0.2)
plt.plot(xline1000ms, yline1000ms,'k--',linewidth=0.2)

plt.xlabel('throughput')
plt.ylabel('latency')
out_png = './delay.png'
plt.savefig(out_png, dpi=400)
# plt.show()