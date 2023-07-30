class SKULL:
  
    ST_BN1_NAME = 'Repo'
    ST_BN1_URL = 'https://github.com/BalaPriyan/skull'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/WZML_X'
    ST_MSG = '''<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own Skull Mirror-Leech bot</i>'''


    BOTSTATS = '''⌬<b><i><u>Bot Statistics</u></i></b>

╭<b>CPU  : </b>{get_progress_bar_string(cpuUsage)} {cpuUsage}
├<code>RAM  : </code>{get_progress_bar_string(mem_p)} {mem_p}
├<code>SWAP : </code>{get_progress_bar_string(swap.percent)} {swap.percent}
╰<code>DISK : </code>{get_progress_bar_string(disk)} {disk}

● <code>Bot Uptime      : </code> {botTime}
● <code>BOT Restart     : </code> {res_time}
● <code>Uploaded        : </code> {sent}
● <code>Downloaded      : </code> {recv}
● <code>Total Bandwidth : </code> {tb}'''

    SYSSTATUS = '''⌬<b><i><u>System Statistics</u></i></b>

● <b>System Uptime:</b> <code>{sysTime}</code>
● <b>P-Core(s):</b> <code>{cpu_count(logical=False)}</code>
● <b>V-Core(s):</b> <code>{v_core}</code>
● <b>Frequency:</b> <code>{cpu_freq(percpu=False).current / 1000:.2f} GHz</code>

╭<b>RAM:</b> {get_progress_bar_string(mem_p)}<code> {mem_p}%</code>
╰<b>Total:</b> <code>{get_readable_file_size(memory.total)}</code>
●<b>Free:</b> <code>{get_readable_file_size(memory.available)}</code>

╭<b>SWAP:</b> {get_progress_bar_string(swap.percent)}<code> {swap.percent}%</code>
╰<b>Total</b> <code>{get_readable_file_size(swap.total)}</code>
● <b>Free:</b> <code>{get_readable_file_size(swap.free)}</code>

╭<b>DISK:</b> {get_progress_bar_string(disk)}<code> {disk}%</code>
╰<b>Total:</b> <code>{total}</code> | <b>Free:</b> <code>{free}</code>'''

    REPOINFO = '''⌬<b><i><u>Repo Info</u></i></b>

╭<code>Updated   : </code> {last_commit}
├<code>Version   : </code> {version}
╰<code>Changelog : </code> {change_log}'''

    BOTLIMIT = '''⌬<b><i><u>Bot Limitations</u></i></b>

╭<code>Torrent   : {TOR}</code> <b>GB</b>
├<code>G-Drive   : {GDL}</code> <b>GB</b>
├<code>Yt-Dlp    : {YTD}</code> <b>GB</b>
├<code>Direct    : {DIR}</code> <b>GB</b>
├<code>Clone     : {CLL}</code> <b>GB</b>
├<code>Leech     : {TGL}</code> <b>GB</b>
╰<code>MEGA      : {MGA}</code> <b>GB</b>

╭<code>User Tasks: {UMT}</code>
╰<code>Bot Tasks : {BMT}</code>'''


