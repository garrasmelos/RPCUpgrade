import FWCore.ParameterSet.Config as cms

def customise_rpcRedigi(process):
    process.load("SimMuon.RPCDigitizer.muonrpcdigi_cfi")

    process.simMuonRPCReDigis = process.simMuonRPCDigis.clone()
    process.simMuonRPCReDigis.digiIRPCModelConfig = cms.PSet(
        Frate = cms.double(1.0),
        Gate = cms.double(25.0),
        IRPC_electronics_jitter = cms.double(0.025),
        IRPC_time_resolution = cms.double(0.05),
        Nbxing = cms.int32(9),
        Rate = cms.double(0.0),
        averageClusterSize = cms.double(1.5),
        averageEfficiency = cms.double(0.95),
        cosmics = cms.bool(False),
        deltatimeAdjacentStrip = cms.double(3.0),
        linkGateWidth = cms.double(20.0),
        printOutDigitizer = cms.bool(False),
        signalPropagationSpeed = cms.double(0.66),
        timeJitter = cms.double(1.0),
        timeResolution = cms.double(2.5),
        timingRPCOffset = cms.double(50.0)
    )

    process.RandomNumberGeneratorService.simMuonRPCReDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(13579),
        engineName = cms.untracked.string('TRandom3')
    )

    process.rpcRecHits.rpcDigiLabel = cms.InputTag("simMuonRPCReDigis")
    process.validationMuonRPCDigis.rpcDigiTag = cms.untracked.InputTag("simMuonRPCReDigis")
    process.reconstruction_step.replace(
        process.rpcRecHits,
        cms.Sequence(process.simMuonRPCReDigis+process.rpcRecHits)
    )

    return process
