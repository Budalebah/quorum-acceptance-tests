package com.quorum.gauge.services;

import com.quorum.gauge.common.QuorumNode;
import com.quorum.gauge.ext.EthSignTransaction;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.core.Request;
import org.web3j.protocol.core.methods.response.EthGetTransactionReceipt;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.quorum.Quorum;
import org.web3j.quorum.methods.request.PrivateTransaction;
import rx.Observable;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Map;
import java.util.Optional;

@Service
public class TransactionService extends AbstractService {
    private static final Logger logger = LoggerFactory.getLogger(TransactionService.class);

    @Autowired
    AccountService accountService;

    @Autowired
    PrivacyService privacyService;

    public Optional<TransactionReceipt> getTransactionReceipt(QuorumNode node, String transactionHash) {
        return getTransactionReceiptObservable(node, transactionHash).toBlocking().first().getTransactionReceipt();
    }

    public Observable<EthGetTransactionReceipt> getTransactionReceiptObservable(QuorumNode node, String transactionHash) {
        Quorum client = connectionFactory.getConnection(node);
        return client.ethGetTransactionReceipt(transactionHash).observable();
    }

    public String sendSignedTransaction(QuorumNode from, QuorumNode to) {
        Web3j client = connectionFactory.getWeb3jConnection(from);
        String fromAddress = accountService.getFirstAccountAddress(from);
        String toAddress = accountService.getFirstAccountAddress(to);
        try {
            PrivateTransaction tx = new PrivateTransaction(fromAddress,
                    null,
                    null,
                    toAddress,
                    BigInteger.valueOf(1),
                    null,
                    Arrays.asList(privacyService.id(to)));
            Request<?, EthSignTransaction> request = new Request<>(
                    "eth_signTransaction",
                    Arrays.asList(tx),
                    connectionFactory.getWeb3jService(from),
                    EthSignTransaction.class
            );
            Map<String, Object> response = request.send().getResult();
            logger.debug("{}", response);
            String rawHexString = (String) response.get("raw");
            return client.ethSendRawTransaction(rawHexString).send().getTransactionHash();
        } catch (Exception e) {
            logger.error("sendSignedTransaction()", e);
            throw new RuntimeException(e);
        }
    }
}
