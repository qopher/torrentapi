def find_info(filename):
    codec = 'x264';
    v = re.search("(?i)(x265|h265|h\.265)",filename);
    if v:
        codec = 'x265';
    v = re.search("(?i)(xvid)",filename);
    if v:
        codec = 'xvid';

    resolution = 'sd';
    a = re.search("(?i)(720p)",filename);
    if a:
        resolution = '720p';
    a = re.search("(?i)(1080p)",filename);
    if a:
        resolution = '1080p';

    source = 'hdtv';
    s = re.search("(?i)(WEB-DL|WEB_DL|WEB\.DL)",filename);
    if s:
        source = 'web-dl';
    s = re.search("(?i)(WEBRIP)",filename);
    if s:
        source = 'webrip';
    s = re.search("(?i)(BRRIP|BDRIP|BluRay)",filename);
    if s:
        source = 'brrip';
    s = re.search("(?i)BluRay(.*)REMUX",filename);
    if s:
        source = 'bluray-remux';
    s = re.search("(?i)BluRay(.*)\.(AVC|VC-1)\.",filename);
    if s:
        source = 'bluray-full';
        
    return_info = []
    return_info.append(codec);
    return_info.append(resolution);
    return_info.append(source);
    return return_info;
