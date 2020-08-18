# -*- coding:utf-8 -*-
TYPE = {'FAR': {'rec_typ': 0, 'rec_sub': 10, 'body': [['CPU_TYPE', 'U1'], ['STDF_VER', 'U1']]},
        'ATR': {'rec_typ': 0, 'rec_sub': 20, 'body': [['MOD_TIM', 'U4'], ['CMD_LINE', 'Cn']]},
        'VUR': {'rec_typ': 0, 'rec_sub': 30, 'body': [['UPD_CNT', 'U1'], ['UPD_NAM', 'K0Cn']]},
        'MIR': {'rec_typ': 1, 'rec_sub': 10,
                'body': [['SETUP_T', 'U4'], ['START_T', 'U4'], ['STAT_NUM', 'U1'], ['MODE_COD', 'C1'],
                         ['RTST_COD', 'C1'], ['PROT_COD', 'C1'], ['BURN_TIM', 'U2'], ['CMOD_COD', 'C1'],
                         ['LOT_ID', 'Cn'], ['PART_TYP', 'Cn'], ['NODE_NAM', 'Cn'], ['TSTR_TYP', 'Cn'],
                         ['JOB_NAM', 'Cn'], ['JOB_REV', 'Cn'], ['SBLOT_ID', 'Cn'], ['OPER_NAM', 'Cn'],
                         ['EXEC_TYP', 'Cn'], ['EXEC_VER', 'Cn'], ['TEST_COD', 'Cn'], ['TST_TEMP', 'Cn'],
                         ['USER_TXT', 'Cn'], ['AUX_FILE', 'Cn'], ['PKG_TYP', 'Cn'], ['FAMLY_ID', 'Cn'],
                         ['DATE_COD', 'Cn'], ['FACIL_ID', 'Cn'], ['FLOOR_ID', 'Cn'], ['PROC_ID', 'Cn'],
                         ['OPER_FRQ', 'Cn'], ['SPEC_NAM', 'Cn'], ['SPEC_VER', 'Cn'], ['FLOW_ID', 'Cn'],
                         ['SETUP_ID', 'Cn'], ['DSGN_REV', 'Cn'], ['ENG_ID', 'Cn'], ['ROM_COD', 'Cn'],
                         ['SERL_NUM', 'Cn'], ['SUPR_NAM', 'Cn']]},
        'MRR': {'rec_typ': 1, 'rec_sub': 20,
                'body': [['FINISH_T', 'U4'], ['DISP_COD', 'C1'], ['USR_DESC', 'Cn'], ['EXC_DESC', 'Cn']]},
        'PCR': {'rec_typ': 1, 'rec_sub': 30,
                'body': [['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['PART_CNT', 'U4'], ['RTST_CNT', 'U4'],
                         ['ABRT_CNT', 'U4'], ['GOOD_CNT', 'U4'], ['FUNC_CNT', 'U4']]},
        'HBR': {'rec_typ': 1, 'rec_sub': 40,
                'body': [['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['HBIN_NUM', 'U2'], ['HBIN_CNT', 'U4'],
                         ['HBIN_PF', 'C1'], ['HBIN_NAM', 'Cn']]},
        'SBR': {'rec_typ': 1, 'rec_sub': 50,
                'body': [['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['SBIN_NUM', 'U2'], ['SBIN_CNT', 'U4'],
                         ['SBIN_PF', 'C1'], ['SBIN_NAM', 'Cn']]},
        'PMR': {'rec_typ': 1, 'rec_sub': 60,
                'body': [['PMR_INDX', 'U2'], ['CHAN_TYP', 'U2'], ['CHAN_NAM', 'Cn'], ['PHY_NAM', 'Cn'],
                         ['LOG_NAM', 'Cn'], ['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1']]},
        'PGR': {'rec_typ': 1, 'rec_sub': 62,
                'body': [['GRP_INDX', 'U2'], ['GRP_NAM', 'Cn'], ['INDX_CNT', 'U2'], ['PMR_INDX', 'K0U2']]},
        'PLR': {'rec_typ': 1, 'rec_sub': 63,
                'body': [['GRP_CNT', 'U2'], ['GRP_INDX', 'K0U2'], ['GRP_MODE', 'K0U2'], ['GRP_RADX', 'K0U1'],
                         ['PGM_CHAR', 'K0Cn'], ['RTN_CHAR', 'K0Cn'], ['PGM_CHAL', 'K0Cn'], ['RTN_CHAL', 'K0Cn']]},
        'RDR': {'rec_typ': 1, 'rec_sub': 70, 'body': [['NUM_BINS', 'U2'], ['RTST_BIN', 'K0U2']]},
        'SDR': {'rec_typ': 1, 'rec_sub': 80,
                'body': [['HEAD_NUM', 'U1'], ['SITE_GRP', 'U1'], ['SITE_CNT', 'U1'], ['SITE_NUM', 'K0U1'],
                         ['HAND_TYP', 'Cn'], ['HAND_ID', 'Cn'], ['CARD_TYP', 'Cn'], ['CARD_ID', 'Cn'],
                         ['LOAD_TYP', 'Cn'], ['LOAD_ID', 'Cn'], ['DIB_TYP', 'Cn'], ['DIB_ID', 'Cn'], ['CABL_TYP', 'Cn'],
                         ['CABL_ID', 'Cn'], ['CONT_TYP', 'Cn'], ['CONT_ID', 'Cn'], ['LASR_TYP', 'Cn'],
                         ['LASR_ID', 'Cn'], ['EXTR_TYP', 'Cn'], ['EXTR_ID', 'Cn']]},
        'PSR': {'rec_typ': 1, 'rec_sub': 90,
                'body': [['CONT_FLG', 'B1'], ['PSR_INDX', 'U2'], ['PSR_NAM', 'Cn'], ['OPT_FLG', 'B1'],
                         ['TOTP_CNT', 'U2'], ['LOCP_CNT', 'U2'], ['PAT_BGN', 'K0U8'], ['PAT_END', 'K0U8'],
                         ['PAT_FILE', 'K0Cn'], ['PAT_LBL', 'K0Cn'], ['FILE_UID', 'K0Cn'], ['ATPG_DSC', 'K0Cn'],
                         ['SRC_ID', 'K0Cn']]},
        'NMR': {'rec_typ': 1, 'rec_sub': 91,
                'body': [['CONT_FLG', 'B1'], ['NMR_INDX', 'U2'], ['TOTM_CNT', 'U2'], ['LOCM_CNT', 'U2'],
                         ['PMR_INDX', 'K0U2'], ['ATPG_NAM', 'K0Cn']]},
        'CNR': {'rec_typ': 1, 'rec_sub': 92, 'body': [['CHN_NUM', 'U2'], ['BIT_POS', 'U4'], ['CELL_NAM', 'Sn']]},
        'SSR': {'rec_typ': 1, 'rec_sub': 93, 'body': [['SSR_NAM', 'Cn'], ['CHN_CNT', 'U2'], ['CHN_LIST', 'K0U2']]},
        'CDR': {'rec_typ': 1, 'rec_sub': 94,
                'body': [['CONT_FLG', 'B1'], ['CDR_INDX', 'U2'], ['CHN_NAM', 'Cn'], ['CHN_LEN', 'U4'],
                         ['SIN_PIN', 'U2'], ['SOUT_PIN', 'U2'], ['MSTR_CNT', 'U1'], ['M_CLKS', 'K0U2'],
                         ['SLAV_CNT', 'U1'], ['S_CLKS', 'K0U2'], ['INV_VAL', 'U1'], ['LST_CNT', 'U2'],
                         ['CELL_LST', 'K0Sn']]},
        'WIR': {'rec_typ': 2, 'rec_sub': 10,
                'body': [['HEAD_NUM', 'U1'], ['SITE_GRP', 'U1'], ['START_T', 'U4'], ['WAFER_ID', 'Cn']]},
        'WRR': {'rec_typ': 2, 'rec_sub': 20,
                'body': [['HEAD_NUM', 'U1'], ['SITE_GRP', 'U1'], ['FINISH_T', 'U4'], ['PART_CNT', 'U4'],
                         ['RTST_CNT', 'U4'], ['ABRT_CNT', 'U4'], ['GOOD_CNT', 'U4'], ['FUNC_CNT', 'U4'],
                         ['WAFER_ID', 'Cn'], ['FABWF_ID', 'Cn'], ['FRAME_ID', 'Cn'], ['MASK_ID', 'Cn'],
                         ['USR_DESC', 'Cn'], ['EXC_DESC', 'Cn']]},
        'WCR': {'rec_typ': 2, 'rec_sub': 30,
                'body': [['WAFR_SIZ', 'R4'], ['DIE_HT', 'R4'], ['DIE_WID', 'R4'], ['WF_UNITS', 'U1'],
                         ['WF_FLAT', 'C1'], ['CENTER_X', 'I2'], ['CENTER_Y', 'I2'], ['POS_X', 'C1'], ['POS_Y', 'C1']]},
        'PIR': {'rec_typ': 5, 'rec_sub': 10, 'body': [['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1']]},
        'PRR': {'rec_typ': 5, 'rec_sub': 20,
                'body': [['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['PART_FLG', 'B1'], ['NUM_TEST', 'U2'],
                         ['HARD_BIN', 'U2'], ['SOFT_BIN', 'U2'], ['X_COORD', 'I2'], ['Y_COORD', 'I2'], ['TEST_T', 'U4'],
                         ['PART_ID', 'Cn'], ['PART_TXT', 'Cn'], ['PART_FIX', 'Bn']]},
        'TSR': {'rec_typ': 10, 'rec_sub': 30,
                'body': [['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['TEST_TYP', 'C1'], ['TEST_NUM', 'U4'],
                         ['EXEC_CNT', 'U4'], ['FAIL_CNT', 'U4'], ['ALRM_CNT', 'U4'], ['TEST_NAM', 'Cn'],
                         ['SEQ_NAME', 'Cn'], ['TEST_LBL', 'Cn'], ['OPT_FLAG', 'B1'], ['TEST_TIM', 'R4'],
                         ['TEST_MIN', 'R4'], ['TEST_MAX', 'R4'], ['TST_SUMS', 'R4'], ['TST_SQRS', 'R4']]},
        'PTR': {'rec_typ': 15, 'rec_sub': 10,
                'body': [['TEST_NUM', 'U4'], ['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['TEST_FLG', 'B1'],
                         ['PARM_FLG', 'B1'], ['RESULT', 'R4'], ['TEST_TXT', 'Cn'], ['ALARM_ID', 'Cn'],
                         ['OPT_FLAG', 'B1'], ['RES_SCAL', 'I1'], ['LLM_SCAL', 'I1'], ['HLM_SCAL', 'I1'],
                         ['LO_LIMIT', 'R4'], ['HI_LIMIT', 'R4'], ['UNITS', 'Cn'], ['C_RESFMT', 'Cn'],
                         ['C_LLMFMT', 'Cn'], ['C_HLMFMT', 'Cn'], ['LO_SPEC', 'R4'], ['HI_SPEC', 'R4']]},
        'MPR': {'rec_typ': 15, 'rec_sub': 15,
                'body': [['TEST_NUM', 'U4'], ['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['TEST_FLG', 'B1'],
                         ['PARM_FLG', 'B1'], ['RTN_ICNT', 'U2'], ['RSLT_CNT', 'U2'], ['RTN_STAT', 'K0N1'],
                         ['RTN_RSLT', 'K0R4'], ['TEST_TXT', 'Cn'], ['ALARM_ID', 'Cn'], ['OPT_FLAG', 'B1'],
                         ['RES_SCAL', 'I1'], ['LLM_SCAL', 'I1'], ['HLM_SCAL', 'I1'], ['LO_LIMIT', 'R4'],
                         ['HI_LIMIT', 'R4'], ['START_IN', 'R4'], ['INCR_IN', 'R4'], ['RTN_INDX', 'K0U2'],
                         ['UNITS', 'Cn'], ['UNITS_IN', 'Cn'], ['C_RESFMT', 'Cn'], ['C_LLMFMT', 'Cn'],
                         ['C_HLMFMT', 'Cn'], ['LO_SPEC', 'R4'], ['HI_SPEC', 'R4']]},
        'FTR': {'rec_typ': 15, 'rec_sub': 20,
                'body': [['TEST_NUM', 'U4'], ['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'], ['TEST_FLG', 'B1'],
                         ['OPT_FLAG', 'B1'], ['CYCL_CNT', 'U4'], ['REL_VADR', 'U4'], ['REPT_CNT', 'U4'],
                         ['NUM_FAIL', 'U4'], ['XFAIL_AD', 'I4'], ['YFAIL_AD', 'I4'], ['VECT_OFF', 'I2'],
                         ['RTN_ICNT', 'U2'], ['PGM_ICNT', 'U2'], ['RTN_INDX', 'K0U2'], ['RTN_STAT', 'K0N1'],
                         ['PGM_INDX', 'K0U2'], ['PGM_STAT', 'K0N1'], ['FAIL_PIN', 'Dn'], ['VECT_NAM', 'Cn'],
                         ['TIME_SET', 'Cn'], ['OP_CODE', 'Cn'], ['TEST_TXT', 'Cn'], ['ALARM_ID', 'Cn'],
                         ['PROG_TXT', 'Cn'], ['RSLT_TXT', 'Cn'], ['PATG_NUM', 'U1'], ['SPIN_MAP', 'Dn']]},
        'STR': {'rec_typ': 15, 'rec_sub': 30,
                'body': [['CONT_FLG', 'B1'], ['TEST_NUM', 'U4'], ['HEAD_NUM', 'U1'], ['SITE_NUM', 'U1'],
                         ['PSR_REF', 'U2'], ['TEST_FLG', 'B1'], ['LOG_TYP', 'Cn'], ['TEST_TXT', 'Cn'],
                         ['ALARM_ID', 'Cn'], ['PROG_TXT', 'Cn'], ['RSLT_TXT', 'Cn'], ['Z_VAL', 'U1'], ['FMU_FLG', 'B1'],
                         ['MASK_MAP', 'Dn'], ['FAL_MAP', 'Dn'], ['CYC_CNT', 'U8'], ['TOTF_CNT', 'U4'],
                         ['TOTL_CNT', 'U4'], ['CYC_BASE', 'U8'], ['BIT_BASE', 'U4'], ['COND_CNT', 'U2'],
                         ['LIM_CNT', 'U2'], ['CYC_SIZE', 'U1'], ['PMR_SIZE', 'U1'], ['CHN_SIZE', 'U1'],
                         ['PAT_SIZE', 'U1'], ['BIT_SIZE', 'U1'], ['U1_SIZE', 'U1'], ['U2_SIZE', 'U1'],
                         ['U3_SIZE', 'U1'], ['UTX_SIZE', 'U1'], ['CAP_BGN', 'U2'], ['LIM_INDX', 'K0U2'],
                         ['LIM_SPEC', 'K0U4'], ['COND_LST', 'K0Cn'], ['CYCO_CNT', 'U2'], ['CYC_OFST', 'K0U8'],
                         ['PMR_CNT', 'U2'], ['PMR_INDX', 'K0U2'], ['CHN_CNT', 'U2'], ['CHN_NUM', 'K0U1'],
                         ['EXP_CNT', 'U2'], ['EXP_DATA', 'K0U1'], ['CAP_CNT', 'U2'], ['CAP_DATA', 'K0U1'],
                         ['NEW_CNT', 'U2'], ['NEW_DATA', 'K0U1'], ['PAT_CNT', 'U2'], ['PAT_NUM', 'K0U1'],
                         ['BPOS_CNT', 'U2'], ['BIT_POS', 'K0U1'], ['USR1_CNT', 'U2'], ['USR1', 'K0U1'],
                         ['USR2_CNT', 'U2'], ['USR2', 'K0U1'], ['USR3_CNT', 'U2'], ['USR3', 'K0U1'], ['TXT_CNT', 'U2'],
                         ['USER_TXT', 'K0U1']]}, 'BPS': {'rec_typ': 20, 'rec_sub': 10, 'body': [['SEQ_NAME', 'Cn']]},
        'EPS': {'rec_typ': 20, 'rec_sub': 20, 'body': []},
        'GDR': {'rec_typ': 50, 'rec_sub': 10, 'body': [['GEN_DATA', 'Vn']]},
        'DTR': {'rec_typ': 50, 'rec_sub': 30, 'body': [['TEXT_DAT', 'Cn']]}}
