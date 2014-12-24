# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: reco --step RAW2DIGI,RECO --conditions START53_V27::All --eventcontent AODSIM --no_exec --mc --filein file:../mc_HLT_RAW/hlt_mc_Run2012.root --fileout aod_mc_Run2012.root --python_filename aod_mc_Run2012.py --number -1
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:../mc_HLT_RAW/hlt_mc_Run2012.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('reco nevts:-1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string( THISROOTFILE ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

process.AODSIMoutput.outputCommands.extend(
        cms.untracked.vstring(
       'keep *_hltActivityPhotonClusterShape_*_*',
       'keep *_hltActivityPhotonEcalIso_*_*',
       'keep *_hltActivityPhotonHcalForHE_*_*',
       'keep *_hltActivityPhotonHcalIso_*_*',
       'keep *_hltCaloJetIDPassed_*_*',
       'keep *_hltElectronActivityDetaDphi_*_*',
       'keep *_hltHitElectronActivityTrackIsol_*_*',
       'keep *_hltKT6CaloJets_rho*_*',
       'keep *_hltL3MuonCandidates_*_*',
       'keep *_hltL3MuonCombRelIsolations_*_*',
       'keep *_hltMetClean_*_*',
       'keep *_hltMet_*_*',
       'keep *_hltPixelMatchElectronsActivity_*_*',
       'keep *_hltPixelVertices_*_*',
       'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*',
       'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
       'keep edmTriggerResults_*_*_*',
       ## RAW data                                                                                                    
       #'keep FEDRawDataCollection_rawDataCollector_*_*',           
       #'keep FEDRawDataCollection_source_*_*', 
       'keep triggerTriggerEvent_*_*_*',
       'keep *_hltL1GtObjectMap_*_*'
            )
          )


# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V27::All', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)

