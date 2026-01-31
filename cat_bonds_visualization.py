#!/usr/bin/env python3
"""
Catastrophe Bonds (Cat Bonds) Visualization
Focus on Global Market and Canada
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set up the figure with multiple subplots
fig = plt.figure(figsize=(20, 24))
fig.suptitle('Catastrophe Bonds (Cat Bonds): Global Market & Canada Focus',
             fontsize=24, fontweight='bold', y=0.98)

# Color palette
colors = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'accent': '#2ca02c',
    'canada': '#d62728',
    'light_blue': '#aec7e8',
    'light_orange': '#ffbb78',
    'dark': '#2c3e50',
    'highlight': '#e74c3c'
}

# ============================================
# 1. GLOBAL CAT BOND MARKET SIZE OVER TIME
# ============================================
ax1 = fig.add_subplot(3, 2, 1)

years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
market_size = [24, 26, 28, 30, 32, 35, 35, 35, 43, 49.5, 61.3]  # Outstanding in billions USD
issuance = [6.5, 7, 10, 9, 11, 8, 12, 10, 15.4, 17.7, 25.6]  # Annual issuance in billions USD

x = np.arange(len(years))
width = 0.35

bars1 = ax1.bar(x - width/2, market_size, width, label='Outstanding Market Size',
                color=colors['primary'], alpha=0.8)
bars2 = ax1.bar(x + width/2, issuance, width, label='Annual Issuance',
                color=colors['secondary'], alpha=0.8)

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Billions USD', fontsize=12)
ax1.set_title('Global Cat Bond Market Growth (2015-2025)', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left')
ax1.grid(axis='y', alpha=0.3)

# Add value labels on 2025 bars
ax1.annotate(f'${market_size[-1]}B', xy=(x[-1] - width/2, market_size[-1]),
             ha='center', va='bottom', fontsize=10, fontweight='bold')
ax1.annotate(f'${issuance[-1]}B', xy=(x[-1] + width/2, issuance[-1]),
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# ============================================
# 2. HOW CAT BONDS WORK - FLOW DIAGRAM
# ============================================
ax2 = fig.add_subplot(3, 2, 2)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('How Catastrophe Bonds Work', fontsize=14, fontweight='bold')

# Draw boxes for entities
def draw_box(ax, x, y, width, height, text, color, text_color='white'):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.05,rounding_size=0.2",
                         facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=10,
            fontweight='bold', color=text_color, wrap=True)

# Main entities
draw_box(ax2, 2, 8, 2.5, 1.2, 'SPONSOR\n(Insurer/Reinsurer)', colors['primary'], 'white')
draw_box(ax2, 5, 5, 2.5, 1.2, 'SPV\n(Special Purpose\nVehicle)', colors['accent'], 'white')
draw_box(ax2, 8, 8, 2.5, 1.2, 'INVESTORS\n(Hedge Funds,\nPensions)', colors['secondary'], 'white')
draw_box(ax2, 5, 2, 2.5, 1.2, 'COLLATERAL\nTRUST', colors['dark'], 'white')

# Arrows with labels
arrow_style = dict(arrowstyle='->', color='black', lw=2)

# Sponsor to SPV (premiums)
ax2.annotate('', xy=(3.8, 5.3), xytext=(2.5, 7.4),
             arrowprops=dict(arrowstyle='->', color=colors['primary'], lw=2))
ax2.text(2.8, 6.5, 'Premiums', fontsize=9, rotation=55, color=colors['primary'])

# Investors to SPV (principal)
ax2.annotate('', xy=(6.2, 5.3), xytext=(7.5, 7.4),
             arrowprops=dict(arrowstyle='->', color=colors['secondary'], lw=2))
ax2.text(7.2, 6.5, 'Principal', fontsize=9, rotation=-55, color=colors['secondary'])

# SPV to Collateral
ax2.annotate('', xy=(5, 2.6), xytext=(5, 4.4),
             arrowprops=dict(arrowstyle='<->', color=colors['accent'], lw=2))
ax2.text(5.2, 3.5, 'Invested\nFunds', fontsize=9, color=colors['accent'])

# SPV to Investors (coupons/principal return)
ax2.annotate('', xy=(7.5, 7.4), xytext=(6.2, 5.5),
             arrowprops=dict(arrowstyle='->', color=colors['accent'], lw=2, linestyle='--'))
ax2.text(7.5, 6.2, 'Coupons +\nPrincipal\n(if no event)', fontsize=8, ha='left')

# SPV to Sponsor (payout if triggered)
ax2.annotate('', xy=(2.5, 7.4), xytext=(3.8, 5.5),
             arrowprops=dict(arrowstyle='->', color=colors['highlight'], lw=2, linestyle='--'))
ax2.text(2.3, 6.2, 'Payout\n(if triggered)', fontsize=8, ha='right', color=colors['highlight'])

# ============================================
# 3. TRIGGER TYPES PIE CHART
# ============================================
ax3 = fig.add_subplot(3, 2, 3)

trigger_types = ['Indemnity\n(Actual Losses)', 'Industry Loss\nIndex', 'Parametric', 'Modeled Loss']
trigger_pcts = [62, 28, 6, 4]
trigger_colors = [colors['primary'], colors['secondary'], colors['accent'], colors['canada']]

wedges, texts, autotexts = ax3.pie(trigger_pcts, labels=trigger_types, autopct='%1.0f%%',
                                    colors=trigger_colors, startangle=90,
                                    explode=(0.05, 0, 0, 0))
ax3.set_title('Cat Bond Trigger Mechanisms', fontsize=14, fontweight='bold')

# ============================================
# 4. CANADA INSURED LOSSES OVER TIME
# ============================================
ax4 = fig.add_subplot(3, 2, 4)

canada_years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
canada_losses = [2.1, 1.3, 2.4, 2.1, 3.1, 3.1, 9.2]  # Billions CAD

bars = ax4.bar(canada_years, canada_losses, color=colors['canada'], alpha=0.8, edgecolor='black')
ax4.axhline(y=4.3, color=colors['dark'], linestyle='--', linewidth=2, label='5-Year Avg (2020-2024): $4.3B')

# Highlight 2024 record
bars[-1].set_color(colors['highlight'])
bars[-1].set_edgecolor('black')
bars[-1].set_linewidth(2)

ax4.set_xlabel('Year', fontsize=12)
ax4.set_ylabel('Billions CAD', fontsize=12)
ax4.set_title('Canada: Insured Losses from Severe Weather', fontsize=14, fontweight='bold')
ax4.legend()
ax4.grid(axis='y', alpha=0.3)

# Add annotation for 2024
ax4.annotate('RECORD\n$9.2B', xy=(2024, 9.2), xytext=(2023.3, 8),
             fontsize=11, fontweight='bold', color=colors['highlight'],
             arrowprops=dict(arrowstyle='->', color=colors['highlight']))

# ============================================
# 5. CANADA'S FIRST CAT BOND - TD INSURANCE
# ============================================
ax5 = fig.add_subplot(3, 2, 5)
ax5.axis('off')
ax5.set_title("Canada's First Cat Bond: TD Insurance (January 2025)",
              fontsize=14, fontweight='bold')

# Create info boxes
info_text = """
+---------------------------------------------------------------+
|                    MMIFS Re Ltd. Series 2025-1                |
+---------------------------------------------------------------+
|  SPONSOR:        TD Insurance                                 |
|                                                               |
|  AMOUNT:         CAD 150 Million                              |
|                                                               |
|  PERILS:         - Earthquake                                 |
|                  - Severe Convective Storm                    |
|                                                               |
|  COVERAGE:       Canadian risks only (first pure-Canada bond) |
|                                                               |
|  TRIGGER:        Indemnity - Per-occurrence basis             |
|                  Attachment: CAD 2.35B losses                 |
|                  Exhaustion: CAD 2.5B losses                  |
|                                                               |
|  TERM:           3 years (Jan 2025 - Dec 2027)                |
|                                                               |
|  COLLATERAL:     CAD-denominated EBRD notes                   |
+---------------------------------------------------------------+
"""

ax5.text(0.5, 0.5, info_text, transform=ax5.transAxes, fontsize=11,
         verticalalignment='center', horizontalalignment='center',
         fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='#f0f0f0',
                                           edgecolor=colors['canada'], linewidth=3))

# ============================================
# 6. KEY STATISTICS & OUTLOOK
# ============================================
ax6 = fig.add_subplot(3, 2, 6)
ax6.axis('off')
ax6.set_title('Cat Bond Market: Key Statistics & 2026 Outlook', fontsize=14, fontweight='bold')

stats_text = """
+------------------------------------------------------------------+
|                     2025 MARKET HIGHLIGHTS                       |
+------------------------------------------------------------------+
|                                                                  |
|  [*] Market Size:    61.3B outstanding (+24% from 2024)          |
|                                                                  |
|  [*] Annual Issuance: 25.6B (+45% YoY, first year over 20B)      |
|                                                                  |
|  [*] Performance:    Swiss Re Cat Bond Index up ~11%             |
|                      (vs 7% corporate bonds, 6% Treasuries)      |
|                                                                  |
|  [*] Wildfire Bonds: 5B issued (2x the 2024 level)               |
|                                                                  |
|  [*] Cyber Bonds:    450M in Q4 2025 (new quarterly record)      |
|                                                                  |
+------------------------------------------------------------------+
|                        2026 OUTLOOK                              |
+------------------------------------------------------------------+
|                                                                  |
|  - Continued market expansion expected                           |
|  - 14B in bonds maturing - providing issuance base               |
|  - New perils: cyber, mortgage, climate-linked risks             |
|  - Geographic expansion: Israel earthquake, more territories     |
|  - Tighter spreads expected (no major 2025 losses)               |
|  - Canada: potential for more sponsors following TD Insurance    |
|                                                                  |
+------------------------------------------------------------------+
"""

ax6.text(0.5, 0.5, stats_text, transform=ax6.transAxes, fontsize=10,
         verticalalignment='center', horizontalalignment='center',
         fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='#e8f4e8',
                                           edgecolor=colors['accent'], linewidth=3))

plt.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.savefig('/home/user/coding-interview-university/cat_bonds_overview.png',
            dpi=150, bbox_inches='tight', facecolor='white')
print("Saved: cat_bonds_overview.png")

# ============================================
# SECOND FIGURE: Canada Deep Dive
# ============================================
fig2 = plt.figure(figsize=(16, 12))
fig2.suptitle('Catastrophe Bonds in Canada: Market Context & Opportunities',
              fontsize=20, fontweight='bold', y=0.98)

# 1. Canada Major Perils
ax_perils = fig2.add_subplot(2, 2, 1)
perils = ['Severe\nConvective\nStorms', 'Wildfires', 'Flooding', 'Earthquakes', 'Winter\nStorms']
peril_exposure = [35, 30, 20, 10, 5]  # Relative exposure/frequency
peril_colors = ['#ff6b6b', '#ffa94d', '#74c0fc', '#845ef7', '#69db7c']

bars = ax_perils.barh(perils, peril_exposure, color=peril_colors, edgecolor='black')
ax_perils.set_xlabel('Relative Risk Exposure (%)', fontsize=12)
ax_perils.set_title('Major Natural Catastrophe Perils in Canada', fontsize=14, fontweight='bold')
ax_perils.grid(axis='x', alpha=0.3)

# Highlight TD bond perils
ax_perils.annotate('TD Cat Bond\nPerils', xy=(35, 0), xytext=(42, 0.7),
                   fontsize=10, fontweight='bold', color=colors['canada'],
                   arrowprops=dict(arrowstyle='->', color=colors['canada']))
ax_perils.annotate('', xy=(10, 3), xytext=(42, 0.7),
                   arrowprops=dict(arrowstyle='->', color=colors['canada']))

# 2. Historical context - losses acceleration
ax_hist = fig2.add_subplot(2, 2, 2)
periods = ['1983-2008\n(Average)', '2009-2020\n(Average)', '2020-2024\n(Average)', '2024\n(Record)']
losses_avg = [0.422, 2.0, 4.3, 9.2]

colors_hist = [colors['light_blue'], colors['primary'], colors['secondary'], colors['highlight']]
bars = ax_hist.bar(periods, losses_avg, color=colors_hist, edgecolor='black', linewidth=2)
ax_hist.set_ylabel('Billions CAD (Annual Average)', fontsize=12)
ax_hist.set_title('Canada: Acceleration of Insured Catastrophe Losses', fontsize=14, fontweight='bold')
ax_hist.grid(axis='y', alpha=0.3)

# Add annotations
for i, (bar, val) in enumerate(zip(bars, losses_avg)):
    ax_hist.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                 f'${val}B', ha='center', fontsize=11, fontweight='bold')

# Add multiplier annotations
ax_hist.annotate('4.7x\nincrease', xy=(0.5, 1.2), xytext=(0.5, 3),
                 fontsize=10, ha='center',
                 arrowprops=dict(arrowstyle='->', color='gray'))
ax_hist.annotate('22x from\nbaseline!', xy=(3, 9.2), xytext=(2.5, 7.5),
                 fontsize=10, ha='center', fontweight='bold', color=colors['highlight'],
                 arrowprops=dict(arrowstyle='->', color=colors['highlight']))

# 3. Why Cat Bonds for Canada - Benefits
ax_benefits = fig2.add_subplot(2, 2, 3)
ax_benefits.axis('off')
ax_benefits.set_title('Why Cat Bonds Matter for Canada', fontsize=14, fontweight='bold')

benefits_text = """
+--------------------------------------------------------------------+
|                        FOR INSURERS                                |
+--------------------------------------------------------------------+
|  [+] Transfer peak catastrophe risks to capital markets            |
|  [+] Multi-year coverage (reduces annual renewal volatility)       |
|  [+] Diversify counterparty risk beyond traditional reinsurers     |
|  [+] Access deep, liquid capital markets                           |
|  [+] Fully collateralized - no credit risk                         |
+--------------------------------------------------------------------+

+--------------------------------------------------------------------+
|                      CANADIAN CONTEXT                              |
+--------------------------------------------------------------------+
|  [!] Insured losses rising exponentially (up 22x since 1980s)      |
|  [!] 2024: Record 9.2B in losses - insurers under pressure         |
|  [!] Climate change increasing frequency/severity of events        |
|  [!] Home insurance becoming unaffordable in high-risk areas       |
|  [!] Some regions losing access to flood/earthquake coverage       |
+--------------------------------------------------------------------+

+--------------------------------------------------------------------+
|                     MARKET OPPORTUNITY                             |
+--------------------------------------------------------------------+
|  [>] TD Insurance success may encourage other Canadian sponsors    |
|  [>] Large insurers with nat-cat exposure are potential issuers    |
|  [>] Regulatory clarity on capital relief would accelerate adoption|
|  [>] Canadian earthquake risk is underinsured - cat bonds can help |
+--------------------------------------------------------------------+
"""

ax_benefits.text(0.5, 0.5, benefits_text, transform=ax_benefits.transAxes, fontsize=10,
                 verticalalignment='center', horizontalalignment='center',
                 fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='#fff5f5',
                                                   edgecolor=colors['canada'], linewidth=2))

# 4. Global vs Canada comparison
ax_compare = fig2.add_subplot(2, 2, 4)

categories = ['Cat Bond\nIssuance\n(2025)', 'Avg Deal\nSize', 'Market\nMaturity', 'Sponsor\nDiversity']
global_scores = [100, 80, 95, 90]  # Normalized scores
canada_scores = [1, 100, 10, 5]    # Relative to global (Canada just started)

x = np.arange(len(categories))
width = 0.35

bars1 = ax_compare.bar(x - width/2, global_scores, width, label='Global Market',
                       color=colors['primary'], alpha=0.8)
bars2 = ax_compare.bar(x + width/2, canada_scores, width, label='Canada',
                       color=colors['canada'], alpha=0.8)

ax_compare.set_ylabel('Relative Score', fontsize=12)
ax_compare.set_title('Canada vs Global Cat Bond Market Development', fontsize=14, fontweight='bold')
ax_compare.set_xticks(x)
ax_compare.set_xticklabels(categories)
ax_compare.legend()
ax_compare.grid(axis='y', alpha=0.3)

# Add annotation
ax_compare.annotate('Room for Growth!\nCanada just issued\nits first cat bond\nin January 2025',
                    xy=(0.5, 1), xytext=(1.5, 50),
                    fontsize=10, ha='center', fontweight='bold', color=colors['canada'],
                    bbox=dict(boxstyle='round', facecolor='#fff0f0'),
                    arrowprops=dict(arrowstyle='->', color=colors['canada']))

plt.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.savefig('/home/user/coding-interview-university/cat_bonds_canada.png',
            dpi=150, bbox_inches='tight', facecolor='white')
print("Saved: cat_bonds_canada.png")

print("\nVisualization complete! Two images generated:")
print("1. cat_bonds_overview.png - Global market overview and how cat bonds work")
print("2. cat_bonds_canada.png - Canada-specific context and opportunities")
