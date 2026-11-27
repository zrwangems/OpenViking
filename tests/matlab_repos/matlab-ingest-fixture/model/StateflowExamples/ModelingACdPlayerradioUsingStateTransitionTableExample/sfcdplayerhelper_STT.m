function sfcdplayerhelper_STT(varargin)
if isa(varargin{1},'Simulink.RunTimeBlock')
    parent_block_name = get_param(varargin{1}.BlockHandle,'Name');
    if strcmp(parent_block_name,'DiscEject')
        set_param('sf_cdplayer_STT/DiscEject','Value','0');
    elseif  strcmp(parent_block_name,'DiscInsert')
        set_param('sf_cdplayer_STT/DiscInsert','Value','0');
    end
elseif ~isa(varargin{1},'Simulink.RunTimeBlock')
    switch(varargin{1})
        case 'set_radio_request'
            sRadioRequest = varargin{2};
            set_param('sf_cdplayer_STT/RR','Value',['RadioRequestMode.' char(RadioRequestMode(sRadioRequest))]);
        case 'set_cd_request'
            sCdRequest = varargin{2};
            set_param('sf_cdplayer_STT/CR','Value',['CdRequestMode.' char(CdRequestMode(sCdRequest))]);
        case 'set_insert_disc'
            set_param('sf_cdplayer_STT/DiscInsert','Value','1');
        case 'set_eject_disc'
            set_param('sf_cdplayer_STT/DiscEject','Value','1');
    end
else
    error('Stateflow:DemoInternalError','Unknown method');
end
end